import cv2
import numpy as np
import serial
import time

# --- CONFIGURACIÓN ---
PUERTO = 'COM4'  # Confirma tu puerto
BAUD   = 115200

# Velocidad de inicio (Bajar)
VELOCIDAD_BAJADA = 150 

try:
    ser = serial.Serial(PUERTO, BAUD, timeout=0.05, write_timeout=0)
    print(f"✅ CONECTADO A {PUERTO} (MODO PID)")
except Exception as e:
    print(f"❌ ERROR: {e}")
    exit()

# CÁMARA
cap = cv2.VideoCapture(1, cv2.CAP_DSHOW) 

# COLORES
bajo1 = np.array([0, 120, 70]); alto1 = np.array([10, 255, 255])
bajo2 = np.array([170, 120, 70]); alto2 = np.array([180, 255, 255])

# INTERFAZ
def nothing(x): pass
cv2.namedWindow("CONTROL PID")
cv2.resizeWindow("CONTROL PID", 600, 600)

# --- SLIDERS PID REFINADOS ---
# Kp: Fuerza Proporcional (0.0 a 5.0) -> Slider 0-500
cv2.createTrackbar("Kp", "CONTROL PID", 150, 500, nothing) 
# Kd: Freno Derivativo (0.0 a 10.0) -> Slider 0-1000
cv2.createTrackbar("Kd", "CONTROL PID", 300, 1000, nothing) 
# Ki: Integral (Usar con cuidado)
cv2.createTrackbar("Ki", "CONTROL PID", 0, 100, nothing) 

# Inversores (Tus valores que ya funcionan)
pol_m1 = 1; pol_m2 = 1; pol_m3 = 1; pol_m4 = 1
def toggle_m1(v): global pol_m1; pol_m1 = -1 if v==1 else 1
def toggle_m2(v): global pol_m2; pol_m2 = -1 if v==1 else 1
def toggle_m3(v): global pol_m3; pol_m3 = -1 if v==1 else 1
def toggle_m4(v): global pol_m4; pol_m4 = -1 if v==1 else 1

cv2.createTrackbar("Inv M1 (InfIzq)", "CONTROL PID", 0, 1, toggle_m1)
cv2.createTrackbar("Inv M2 (InfDer)", "CONTROL PID", 0, 1, toggle_m2)
cv2.createTrackbar("Inv M3 (SupDer)", "CONTROL PID", 0, 1, toggle_m3)
cv2.createTrackbar("Inv M4 (SupIzq)", "CONTROL PID", 0, 1, toggle_m4)

# ==========================================
#   FASE 1: CALIBRACIÓN (15s)
# ==========================================
print("⬇️ BAJANDO PLATAFORMA...")
start_cal = time.time()

while (time.time() - start_cal) < 15:
    ret, frame = cap.read()
    if not ret: break
    frame = cv2.resize(frame, (640, 480))
    
    if ser.is_open:
        msg = f"{VELOCIDAD_BAJADA},{VELOCIDAD_BAJADA},{VELOCIDAD_BAJADA},{VELOCIDAD_BAJADA}\n"
        ser.write(msg.encode())
    
    time_left = 15 - int(time.time() - start_cal)
    cv2.putText(frame, f"CALIBRANDO: {time_left}s", (50, 240), 
                cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 255), 3)
    cv2.imshow("CONTROL PID", frame)
    if cv2.waitKey(10) & 0xFF == ord('q'): exit()

# Frenar antes de empezar
if ser.is_open:
    ser.write(b"0,0,0,0\n")
    time.sleep(0.2)

print("🏁 INICIANDO CONTROL PID.")

# ==========================================
#   FASE 2: BUCLE PID
# ==========================================
last_send = 0
last_err_x = 0
last_err_y = 0
integ_x = 0
integ_y = 0
last_time_pid = time.time()

while True:
    ret, frame = cap.read()
    if not ret: break
    
    # Procesar imagen más chica para velocidad, dibujar en grande
    proc_frame = cv2.resize(frame, (320, 240)) 
    h, w, _ = proc_frame.shape
    cx, cy = w // 2, h // 2

    # Leer Sliders (Escalados)
    Kp = cv2.getTrackbarPos("Kp", "CONTROL PID") / 100.0  # Ej: 150 -> 1.5
    Kd = cv2.getTrackbarPos("Kd", "CONTROL PID") / 100.0  # Ej: 300 -> 3.0
    Ki = cv2.getTrackbarPos("Ki", "CONTROL PID") / 1000.0 # Muy pequeño

    hsv = cv2.cvtColor(proc_frame, cv2.COLOR_BGR2HSV)
    mask = cv2.add(cv2.inRange(hsv, bajo1, alto1), cv2.inRange(hsv, bajo2, alto2))
    mask = cv2.erode(mask, None, iterations=1)
    mask = cv2.dilate(mask, None, iterations=2)
    
    cnts, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    m1=0; m2=0; m3=0; m4=0
    ball_found = False

    # Tiempo delta para PID preciso
    current_time = time.time()
    dt = current_time - last_time_pid
    if dt == 0: dt = 0.001
    last_time_pid = current_time

    if len(cnts) > 0:
        c = max(cnts, key=cv2.contourArea)
        ((x, y), r) = cv2.minEnclosingCircle(c)
        
        if r > 4: # Radio mínimo en imagen pequeña
            ball_found = True
            
            # Dibujar en cuadro original (multiplicar x2 coord)
            cv2.circle(frame, (int(x)*2, int(y)*2), int(r)*2, (0, 255, 0), 2)
            cv2.line(frame, (cx*2, cy*2), (int(x)*2, int(y)*2), (255, 0, 0), 2)

            # --- CÁLCULO PID ---
            # Error = Distancia al centro
            err_x = int(x - cx)
            err_y = int(y - cy)
            
            # PID X
            # Derivada = (Error actual - Error anterior) / tiempo
            d_x = (err_x - last_err_x) / dt
            # Integral = Acumulado + Error * tiempo
            integ_x = max(min(integ_x + (err_x * dt), 200), -200) # Anti-windup
            
            output_x = (err_x * Kp) + (d_x * Kd) + (integ_x * Ki)
            last_err_x = err_x
            
            # PID Y
            d_y = (err_y - last_err_y) / dt
            integ_y = max(min(integ_y + (err_y * dt), 200), -200)
            
            output_y = (err_y * Kp) + (d_y * Kd) + (integ_y * Ki)
            last_err_y = err_y
            
            # --- MEZCLA DE MOTORES ---
            # Lógica: Si Output > 0, es fuerza positiva (BAJAR lado correspondiente)
            # Si Output < 0, es fuerza negativa (SUBIR lado correspondiente)
            
            # X: +Out -> Bajar Izq, Subir Der
            # Y: +Out -> Bajar Arr, Subir Abj
            
            m1 = int( -output_y + output_x ) # Inf Izq
            m2 = int( -output_y - output_x ) # Inf Der
            m3 = int(  output_y - output_x ) # Sup Der
            m4 = int(  output_y + output_x ) # Sup Izq
            
            # Limitar PWM (-255 a 255)
            m1 = max(min(m1, 255), -255)
            m2 = max(min(m2, 255), -255)
            m3 = max(min(m3, 255), -255)
            m4 = max(min(m4, 255), -255)

    # ENVÍO DE DATOS RÁPIDO (cada 15ms -> ~60Hz)
    if ser.is_open and (time.time() - last_send > 0.015):
        try:
            if not ball_found:
                msg = "0,0,0,0\n" # Si no veo la pelota, no me muevo
            else:
                msg = f"{m1*pol_m1},{m2*pol_m2},{m3*pol_m3},{m4*pol_m4}\n"
            
            ser.write(msg.encode())
            last_send = time.time()
            
            # Mostrar valores PID en pantalla
            info = f"P:{Kp:.2f} D:{Kd:.2f} | OutX:{int(output_x)}"
            cv2.putText(frame, info, (10, 450), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)
        except: pass

    cv2.imshow("CONTROL PID", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'): break

if ser.is_open:
    ser.write(b"0,0,0,0\n")
    ser.close()
cv2.destroyAllWindows()