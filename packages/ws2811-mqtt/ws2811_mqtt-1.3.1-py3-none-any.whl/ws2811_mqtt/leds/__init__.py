import board
import neopixel
import os
import threading  # For running the alternating color loop
import time
import random

from ws2811_mqtt.logger import log_client


NUM_LEDS = int(os.getenv("NUM_LEDS") or 50) # Number

# Initialize the NeoPixel strip
pixels = neopixel.NeoPixel(board.D18, NUM_LEDS, brightness=1, auto_write=os.getenv("AUTOWRITE") == "True" or False)
leds = [{"state": "OFF", "color": (255,255,255)} for _ in range(len(pixels))]
# pixels = [(0, 0, 0) for _ in range(NUM_LEDS)]

loop_thread = None
loop_active = False
last_state = -1

colors_options = {
    "color_one": (255,255,0),
    "color_two": (0,255,255),
    "rate": 2,
    "transition": True,
    "loop_type": "alternate"
}

def set_cc_options(opt_object):
    global colors_options
    global loop_active

    if loop_active:
        stop_loop()
    log_client.info(f"[LEDS][%15s] set_cc_options called with obj={opt_object}", "set_cc_options")
    if opt_object:
        colors_options = {**colors_options, **opt_object}
        start_loop()


def manage_loop():
    global loop_active
    global colors_options
    global last_state
    try:
        state = -last_state
        log_client.info(f"[LEDS][%15s] State: {loop_active}", "manage_loop")
        while loop_active:
            if colors_options.get("loop_type") == "alternate":
                state = -state
                for i in range(NUM_LEDS):
                    state = -state
                    set_l_on(i, colors_options.get("color_one") if state == 1 else colors_options.get("color_two"))
                    if colors_options.get("transition"):
                        if not pixels.auto_write:
                            pixels.show()
                        time.sleep(colors_options.get("rate") / NUM_LEDS)
                    if not loop_active:
                        break
                if not pixels.auto_write:
                    pixels.show()
                log_client.info(f"[LEDS][%15s] state => {state}", "manage_loop")
                total_wait_time = colors_options.get("rate")
                elapsed_time = 0
                while elapsed_time < total_wait_time:
                    if not loop_active:
                        break
                    time.sleep(0.5)  # Check every second
                    elapsed_time += 0.5
            elif colors_options.get("loop_type") == "cycle":
                state = -state
                for i in range(NUM_LEDS):
                    set_l_on(i, colors_options.get("color_one") if state == 1 else colors_options.get("color_two"))
                    if colors_options.get("transition"):
                        time.sleep(colors_options.get("rate") / NUM_LEDS)
                        if not pixels.auto_write:
                            pixels.show()
                    if not loop_active:
                        break
                log_client.info(f"[LEDS][%15s] state => {state}", "manage_loop")
                if not colors_options.get("transition"):
                    if not pixels.auto_write:
                        pixels.show()
                total_wait_time = colors_options.get("rate")
                elapsed_time = 0
                while elapsed_time < total_wait_time:
                    if not loop_active:
                        break
                    time.sleep(0.5)  # Check every second
                    elapsed_time += 0.5
            elif colors_options.get("loop_type") == "fireplace":
                steps_per_second = 15  # Number of steps between colors per second
                total_steps = int(colors_options.get("rate") * steps_per_second)
                step_duration = 1.0 / steps_per_second
                final_colors = []  # Store final colors for each LED
                for i in range(NUM_LEDS):
                    # Generate random reddish-yellowish colors for final step
                    red = random.randint(150, 255)
                    green = random.randint(50, 100)
                    blue = random.randint(0, 50)
                    brightness = random.uniform(0.5, 1.0)

                    # Apply brightness factor
                    target_green = int(green * brightness)
                    target_red = int(red * brightness)
                    target_blue = int(blue * brightness)
                    final_colors.append((target_green, target_red, target_blue))
                    if not loop_active:
                        break


                for current_step in range(total_steps):
                    for i in range(NUM_LEDS):
                        # Get the current color
                        current_color = leds[i]["color"]
                        cur_green, cur_red, cur_blue = current_color

                        # Determine target color for final step
                        target_green, target_red, target_blue = final_colors[i]

                        # Transition between current and target color
                        intermediate_red = int(cur_red + (target_red - cur_red) * (current_step / total_steps))
                        intermediate_green = int(cur_green + (target_green - cur_green) * (current_step / total_steps))
                        intermediate_blue = int(cur_blue + (target_blue - cur_blue) * (current_step / total_steps))

                        # Apply the new intermediate color
                        set_l_on(i, (intermediate_green, intermediate_red, intermediate_blue))
                        if not loop_active:
                            break
                    if not pixels.auto_write:
                        pixels.show()
                    # Wait for the next step
                    time.sleep(step_duration)

                # Ensure LEDs show the final color for a full cycle before restarting
                for i in range(NUM_LEDS):
                    set_l_on(i, final_colors[i])
                if not pixels.auto_write:
                    pixels.show()
                total_wait_time = colors_options.get("rate")
                elapsed_time = 0
                while elapsed_time < total_wait_time:
                    time.sleep(0.5)  # Hold final color for the remaining time of the cycle
                    elapsed_time += 0.5
            else:
                break
    except Exception as e:
        log_client.error(f"[LEDS][%15s] Error in alternating colors: {e}", "manage_loop")

def start_loop():
    global loop_thread, loop_active, colors_options
    if loop_thread is not None and loop_thread.is_alive():
        stop_loop()
        loop_thread.join()  # Ensure the previous thread ends before starting a new one
    loop_active = True
    loop_thread = threading.Thread(target=manage_loop, args=())
    loop_thread.start()

def stop_loop():
    global loop_active
    loop_active = False
    log_client.info(f"[LEDS][%15s] Before joining the thread", "stop_loop")
    if loop_thread is not None:
        loop_thread.join()
    log_client.info(f"[LEDS][%15s] After joining thread", "stop_loop")

# Function to apply changes from the leds array to the pixels array
def set_led(led_index):
    try:
        if leds[led_index]["state"] == "OFF":
            pixels[led_index] = (0, 0, 0)
        else:
            pixels[led_index] = leds[led_index]["color"]
            log_client.debug(f"[LEDS][%15s] {led_index} => {leds[led_index]['state']}", "set_led")
    except Exception as e:
        log_client.error(f"[LEDS][%15s] Error applying LED changest to led {led_index}: {e}", "set_led")


# Function to check if an LED is on by verifying its color is not black (0, 0, 0)
def led_is_on(led_index):
    log_client.debug(f"[LEDS][%15s] LED index {led_index}", "led_is_on")
    log_client.debug(f"[LEDS][%15s] LED value {pixels[led_index]}", "led_is_on")
    led_on = leds[led_index]["state"] == "ON"
    return led_on

# Function to set a LED's color to black (0, 0, 0), effectively turning it off
def set_l_off(led_index):
    try:
        log_client.debug(f"[LEDS][%15s] LED value before {pixels[led_index]}", "set_l_off")
        pixels[led_index] = (0, 0, 0)
        log_client.debug(f"[LEDS][%15s] LED {led_index} color set to black.", "set_l_off")
        log_client.debug(f"[LEDS][%15s] LED value after  {pixels[led_index]}", "set_l_off")
    except Exception as e:
        log_client.error(f"[LEDS][%15s] Error setting LED color: {e}", "set_l_off")

# Function to set a LED's color to a specified value, defaulting to white (255, 255, 255)
def set_l_on(led_index, color=None):
    try:
        leds[led_index].update({"state": "ON", "color": color or leds[led_index]["color"]})
        set_led(led_index)
        log_client.debug(f"[LEDS][%15s] LED {led_index} color set to {color}.", "set_l_on")
    except Exception as e:
        log_client.error(f"[LEDS][%15s] Error setting LED color: {e}", "set_l_on")
