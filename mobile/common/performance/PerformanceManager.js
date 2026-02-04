import { PerformanceObserver, performance } from 'react-native-performance';

export class PerformanceManager {
    constructor() {
        this.observer = new PerformanceObserver((list) => {
            const entries = list.getEntries();
            entries.forEach((entry) => {
                console.log(`Performance Entry: ${entry.name} - ${entry.duration}`);
            });
        });
        this.observer.observe({ entryTypes: ['measure'] });
    }

    static markStart(name) {
        performance.mark(`${name}-start`);
    }

    static markEnd(name) {
        performance.mark(`${name}-end`);
        performance.measure(name, `${name}-start`, `${name}-end`);
    }
}

export default new PerformanceManager();