export class Snake {
    constructor(position, direction) {
        this.position = position;
        this.direction = direction;
        this.speed = 1; // Units per update
    }

    update() {
        this.position.x += this.direction.x * this.speed;
        this.position.y += this.direction.y * this.speed;
    }

    changeDirection(newDirection) {
        // Prevent reversing direction
        if (this.direction.x + newDirection.x !== 0 || this.direction.y + newDirection.y !== 0) {
            this.direction = newDirection;
        }
    }
}
