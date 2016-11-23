package main

import (
	"time"

	"github.com/hybridgroup/gobot"
	"github.com/hybridgroup/gobot/platforms/gpio"
	"github.com/hybridgroup/gobot/platforms/raspi"
)

func main() {
	gbot := gobot.NewGobot()

	pi := raspi.NewRaspiAdaptor("pi")
	led := gpio.NewLedDriver(pi, "led", "3")

	work := func() {
		gobot.Every(1*time.Second, func() {
			led.Toggle()
		})
	}

	robot := gobot.NewRobot("bot",
		[]gobot.Connection{pi},
		[]gobot.Device{led},
		work,
	)
	gbot.AddRobot(robot)
	gbot.Start()
}
