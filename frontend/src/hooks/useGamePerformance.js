import { useEffect, useState } from 'react';

const useGamePerformance = () => {
    const [performanceMetrics, setPerformanceMetrics] = useState({});

    useEffect(() => {
        const handleResize = () => {
            // Throttle performance adjustments
            setPerformanceMetrics(prevMetrics => ({
                ...prevMetrics,
                adjusted: true // Example flag for adjusted metrics
            }));
        };

        window.addEventListener('resize', handleResize);

        return () => {
            window.removeEventListener('resize', handleResize);
        };
    }, []);

    return performanceMetrics;
};

export default useGamePerformance;