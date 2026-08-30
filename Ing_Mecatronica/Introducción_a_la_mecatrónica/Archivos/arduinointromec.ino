#include "BluetoothSerial.h"

float Kp=0.2;
String device_name = "ESP32_ANA";

// Check if Bluetooth is available
#if !defined(CONFIG_BT_ENABLED) || !defined(CONFIG_BLUEDROID_ENABLED)
#error Bluetooth is not enabled! Please run `make menuconfig` to and enable it
#endif

// Check Serial Port Profile
#if !defined(CONFIG_BT_SPP_ENABLED)
#error Serial Port Profile for Bluetooth is not available or not enabled. It is only available for the ESP32 chip.
#endif

BluetoothSerial SerialBT;
String msj="";
String errorx="";
String errory="";


void setup() {
  Serial.begin(115200);
  SerialBT.begin(device_name);  //Bluetooth device name
  //SerialBT.deleteAllBondedDevices(); // Uncomment this to delete paired devices; Must be called after begin
  Serial.printf("The device with name \"%s\" is started.\nNow you can pair it with Bluetooth!\n", device_name.c_str());
}

void loop() {
  if (Serial.available()) {
    msj = Serial.readStringUntil('\n');
    errorx=msj.substring(0,msj.indexOf(','));
    errory=msj.substring(msj.indexOf(',')+1);
    int x=errorx.toInt();
    int y=errory.toInt();
    Serial.println(x);
    Serial.println(y);
  }


  delay(20);
}
