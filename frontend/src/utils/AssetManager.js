export const loadAssetsAsync = async () => {
  const assets = [
    // List of asset URLs or paths
    '/assets/sprite1.png',
    '/assets/sprite2.png',
    // ...more assets
  ];

  const assetPromises = assets.map(async (asset) => {
    const response = await fetch(asset);
    if (!response.ok) {
      throw new Error(`Failed to load asset: ${asset}`);
    }
    return await response.blob();
  });

  return Promise.all(assetPromises);
};
