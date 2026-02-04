import { Snake } from './snake';
import { InputHandler } from './inputHandler';

const snake = new Snake({ x: 10, y: 10 }, { x: 1, y: 0 });
new InputHandler(snake);

function gameLoop(timestamp) {
    // Fixed timestep for consistent speed
    window.requestAnimationFrame(gameLoop);
    snake.update();
    // Additional rendering code would go here
}

window.requestAnimationFrame(gameLoop);
