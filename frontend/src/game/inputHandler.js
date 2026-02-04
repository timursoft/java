export class InputHandler {
    constructor(snake) {
        this.snake = snake;
        this.keyMap = {
            ArrowUp: { x: 0, y: -1 },
            ArrowDown: { x: 0, y: 1 },
            ArrowLeft: { x: -1, y: 0 },
            ArrowRight: { x: 1, y: 0 }
        };
        window.addEventListener('keydown', this.handleKeyDown.bind(this));
    }

    handleKeyDown(event) {
        const newDirection = this.keyMap[event.key];
        if (newDirection) {
            this.snake.changeDirection(newDirection);
        }
    }
}
