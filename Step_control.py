# import time
import threading

def step_sorting(visualizer, algorithm_function, data, root, code_display):
    visualizer.step_mode = True  
    visualizer.current_step = 0  
    visualizer.step_history = [list(data)]  # Store initial state

    def run():
        algorithm_function(visualizer, data, root, code_display, step_by_step=True)
    
    threading.Thread(target=run).start()

def step_searching(visualizer, algorithm_function, data, target, root, code_display):
    visualizer.step_mode = True
    visualizer.current_step = 0
    visualizer.step_history = [list(data)]

    def run():
        algorithm_function(visualizer, data, target, root, code_display, step_by_step=True)
    
    threading.Thread(target=run).start()

def next_step(visualizer):
    if visualizer.step_mode:
        visualizer.current_step += 1  
        visualizer.step_event.set()  

def prev_step(visualizer):
    if visualizer.step_mode and visualizer.current_step > 0:
        visualizer.current_step -= 1  
        prev_data = visualizer.step_history[visualizer.current_step]  # Get previous state
        visualizer.data = list(prev_data)  
        visualizer.update_plot(visualizer.data, ["blue"] * len(visualizer.data))  
