# Beauty Is More Than Skin Deep: A Design Diary by Tim Burrell-Saward
**Update #31 — June 19, 2020**
*Restoration Games*
**Source:** https://www.kickstarter.com/projects/restorationgames/return-to-dark-tower/posts/2870044

---

*The last time our lead Tower designer, Tim Burrell-Saward, stopped by, he took a nice long look at the aesthetics of the Tower design. This time around, we're stripping off the swanky shell and taking a nice long look at the guts of this thing. Take it away, Tim:*

---

When I posted my last tower update back in January we were coming to the end of the Kickstarter and beginning to gear up to actually start making the game. After the frantic whirlwind that was the campaign, everyone was looking forward to a slightly more relaxed period of work. But then the world decided to slide into the toilet and Normal Operating Procedures went out the window.

Because you're not truly suffering for your art until you're juggling an incredibly complex mechatronic project with an international team (operating across borderline incompatible timezones), whilst also trying to navigate the end of the world. We are indeed living in interesting times.

Nevertheless, a lot has been going on in terms of tower development. Here's an update.

---

## Design for Manufacture (DFM)

In February we put the tower prototype under the microscope and started to do all of the detail work needed to get it ready for manufacture. This part of the process is called **Design for Manufacture (DFM)**, and involves a great deal of collaboration with engineers in our partner factories in China, to ensure that the design we take to production is as reliable, strong and safe as possible.

DFM is a fraught-yet-satisfying part of the manufacturing process, as you need to balance artistic desires with the cold hard realities of Making Things Real. Every decision becomes a balancing act between opposing forces:

- Form vs. function
- Time vs. money
- Spectacle vs. reliability
- Magic vs. physics

Every game you own, film you watch and book you read has been through a similar battle. The fight is great and terrible, and I love it and hate it.

---

## The Gearboxes

A large part of DFM is about identifying potential failure points and designing them out, and it'll come as no surprise that the gearboxes were top of the list of Things That Could Go Wrong. When making prototypes, you tend to make a lot of decisions based on the components and fabrication methods you have to hand. Things like tiny gears may not 3D print very well, which can result in creaky, groaning mechanisms that, whilst sounding very atmospheric, aren't particularly reliable.

DFM allowed us to redesign the gearboxes for mass manufacture, balancing factors like size, cost and rotation speed. The same is true for the gearbox housing, which holds all of the gears nice and tightly in place:

- With the **prototype**: we designed a housing that allowed us to adjust the position of the parts, so that we could make changes on the fly
- During **DFM**: we lock the gears in place and design the housings to keep all the parts exactly where we need them to be, to make sure the gears don't skip or jam

We test motors to make sure they'll last as long as we need them to. We adjust gear ratios to give us the exact rotation speed we want, and we choose the right materials for each part to make sure they last.

![Gearbox Assembly](images/post_2870044_beauty_is_more_than_skin_deep_tim_burrell_saward/3e6e2cab3b55287f2adbeb4d1e56282e_original.jpg)

---

## The Rotating Drums — Optical Sensors

For the rotating drums, the challenge was to find the most robust and reliable way of keeping track of the drum rotations throughout the game, to make sure the app always knows which glyphs and openings are facing which direction.

For the Kickstarter prototype we used tiny **microswitches**, which were tripped by a system of ramps attached to the base of the drums. Each time the switch was tripped the tower knew that the doorways were aligned, and would instantly stop the motor. This system functioned as needed, but we were concerned that a lifetime of flicking those little switches might end in them breaking.

The solution we've ended up with was to switch to a **photo-reflector** — a tiny optical sensor consisting of an infra-red LED emitter sat next to a receiver, both pointing in the same direction. The LED casts out infra-red light, some of which bounces back onto the receiver generating a current that we can measure.

We've installed a photo-reflector above each drum (pointing down) and have created a pattern of reflective stripes directly below it on the drum's lid. When the drum rotates and a reflective stripe passes underneath the sensor, the amount of infra-red light bouncing back changes, letting us know that a trigger has been hit and the motor needs to stop.

![Old Microswitch vs. New Photo-Reflector Design](images/post_2870044_beauty_is_more_than_skin_deep_tim_burrell_saward/eaa9fd3c47a47591b9995c3c852c7b10_original.jpg)

This gives us the speed and sensitivity we need to make sure the drums stop in the right place — but without any physical wear and tear on the switch. Magic!

![Outdoor Photo-Reflector Sunlight Test](images/post_2870044_beauty_is_more_than_skin_deep_tim_burrell_saward/f90de502046455ad050c61a897d11cfb_original.jpg)

---

## The Doorways — Eliminating Skull Jams

For the doorways, the challenge was to remove any chance that skulls might become trapped and cause jamming when the drums rotate. Frankly, this happened more than I was willing to accept with the Kickstarter prototype.

This demonstrates the importance of prototyping designs before they go to production — so you can test and iterate as you go. Sometimes things look like they'll work fine on a screen, but it's only when you have them in your hands that you have the full picture.

The answer was to go back to the drawing board and completely revise the way the drums interface with the outer shell. And because we're dealing with some very precise tolerances, a change to one part can quickly snowball into a whole heap of extra work. But we're confident the risk has been mitigated, and will keep testing and revising until we're certain.

![Doorway Tolerance Detail](images/post_2870044_beauty_is_more_than_skin_deep_tim_burrell_saward/f6509fc06a3828d0252de2601b95b88c_original.jpg)

---

## Electronics — Sound and Light

**Sound**: The balance has involved trying to get the highest volume and best quality audio out of the limited physical space we have. The speaker is located right at the base of the tower and pointed upwards, causing the body of the tower to amplify the speaker's output. The small space means we can't have a huge speaker, so we have to be clever with the components we use. It's also powered from the same supply as the LEDs, which means our electronics engineer Charlie has had to do some additional wizardry to make sure there isn't any electrical interference that translates into weird audio noise.

![Prototype PCB Panel](images/post_2870044_beauty_is_more_than_skin_deep_tim_burrell_saward/c9bcb95aac80398fc02552b97b5a48e9_original.png)

**Light**: We've been working on maximising the light output from the **24 individually addressable red LEDs** dotted around the tower, to give the most atmospheric light show we can give without draining the batteries too fast. Work is still ongoing but we're really happy with what we're achieving here.

![Tower Dark Heart (Internal Electronics)](images/post_2870044_beauty_is_more_than_skin_deep_tim_burrell_saward/755fe263ed00c85e791e71153152a10b_original.jpg)

---

## What's Next

We're coming to the end of the DFM process now, but there are a few things to finish off before we can start making the injection moulding tools:

- Skull distribution testing (to make sure probabilities still hold true)
- Outer shell texturing (for the gnarled, weathered look)
- Colour and transparency decisions
- Firmware tidy-up and bug squishing
- Packaging progression
- And the other thousand-and-one things on the list

But once all this is done — which shouldn't be too much longer — we'll be ready for the really, really fun bit: **making things real**.

![Transparent Tooling Model — Full Tower](images/post_2870044_beauty_is_more_than_skin_deep_tim_burrell_saward/6946646bcecaecc6845d86c0742e67b4_original.jpg)