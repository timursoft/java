/**
 * gestureHandler.js
 * Utility functions to handle gesture detection
 */

export function detectSwipeDirection(startX, startY, endX, endY) {
    const dx = endX - startX;
    const dy = endY - startY;

    if (Math.abs(dx) > Math.abs(dy)) {
        if (dx > 0) {
            return 'right';
        } else {
            return 'left';
        }
    } else {
        if (dy > 0) {
            return 'down';
        } else {
            return 'up';
        }
    }
}

export function handleSwipe(event, onSwipeLeft, onSwipeRight, onSwipeUp) {
    const touch = event.changedTouches[0];
    const startX = touch.clientX;
    const startY = touch.clientY;

    event.target.addEventListener('touchend', function onEnd(e) {
        const endX = e.changedTouches[0].clientX;
        const endY = e.changedTouches[0].clientY;
        const direction = detectSwipeDirection(startX, startY, endX, endY);

        switch (direction) {
            case 'left':
                onSwipeLeft();
                break;
            case 'right':
                onSwipeRight();
                break;
            case 'up':
                onSwipeUp();
                break;
        }

        event.target.removeEventListener('touchend', onEnd);
    });
}