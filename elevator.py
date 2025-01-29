def elevator_agent(current_floor, call_buttons, previous_states):
    for floor, button_pressed in enumerate(call_buttons):
        if button_pressed and not previous_states[floor]: 
           
            previous_states[floor] = True
            if floor > current_floor:
                return "move up", previous_states
            elif floor < current_floor:
                return "move down", previous_states
            else:
                return "stay stationary", previous_states
    
    return "stay stationary", previous_states  

def main():
    num_floors = 5
    current_floor = 0
    previous_states = [False] * num_floors  

    scenarios = [
        [False, True, False, False, False],  
        [False, False, True, False, False],  
        [False, False, False, False, False],  
        [False, False, False, True, False], 
    ]

    for call_buttons in scenarios:
        print(f"Before action: Current Floor: {current_floor}, Previous States: {previous_states}")
        action, previous_states = elevator_agent(current_floor, call_buttons, previous_states)
        print(f"Action: {action}, Previous States: {previous_states}")
      
        if action == "move up":
            current_floor += 1
        elif action == "move down":
            current_floor -= 1

        print(f"After action: Current Floor: {current_floor}, Previous States: {previous_states}\n")


if __name__ == "__main__":
    main()