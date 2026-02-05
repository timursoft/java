import { useCallback } from 'react';
import { toast } from 'react-toastify';

export const useTapHandler = () => {
  const handleTap = useCallback((event) => {
    // Implement the logic for single tap
    toast('Single tap detected!');
  }, []);

  const handleDoubleTap = useCallback((event) => {
    // Implement the logic for double tap
    toast('Double tap detected!');
  }, []);

  return { handleTap, handleDoubleTap };
};
