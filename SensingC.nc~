#include "StorageVolumes.h"

configuration SensingC {

} implementation {
	components MainC, LedsC, SensingP;
	SensingP.Boot -> MainC;
	SensingP.Leds -> LedsC;

	components IPStackC;
	components RPLRoutingC;
	components StaticIPAddressTosIdC;
	SensingP.RadioControl -> IPStackC;

	components new UdpSocketC() as Settings;
	SensingP.Settings -> Settings;
        
	components new UdpSocketC() as Initial;
	SensingP.Initial -> Initial;

	components new UdpSocketC() as ReportCounter;
	SensingP.ReportCounter -> ReportCounter;
       
	components UDPShellC;
	components new ShellCommandC("get") as GetCmd;
	components new ShellCommandC("set") as SetCmd;
	SensingP.GetCmd -> GetCmd;
	SensingP.SetCmd -> SetCmd;

	components new HamamatsuS1087ParC() as SensorPar;
	SensingP.StreamPar -> SensorPar.ReadStream;

	components new TimerMilliC() as RandomTimer;
	SensingP.RandomTimer -> RandomTimer;

	components new TimerMilliC() as SampleTimer;
	SensingP.SampleTimer-> SampleTimer;

        components new TimerMilliC() as BlinkTimer;
	SensingP.BlinkTimer -> BlinkTimer;

	components new ConfigStorageC(VOLUME_CONFIG) as LocalSettings;
	SensingP.ConfigMount -> LocalSettings;
	SensingP.ConfigStorage -> LocalSettings;

}
