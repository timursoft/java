<template>
  <div id="game-environment">
    <Skybox :texture="skyboxTexture" />
    <Terrain :heightMap="terrainHeightMap" />
    <Lighting :settings="lightingSettings" />
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex';
import Skybox from './Skybox.vue';
import Terrain from './Terrain.vue';
import Lighting from './Lighting.vue';

export default {
  components: {
    Skybox,
    Terrain,
    Lighting
  },
  computed: {
    ...mapState('gameEnvironment', ['skyboxTexture', 'terrainHeightMap', 'lightingSettings'])
  },
  methods: {
    ...mapActions('gameEnvironment', ['fetchEnvironmentAssets'])
  },
  created() {
    this.fetchEnvironmentAssets();
  }
};
</script>

<style scoped>
#game-environment {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height: 100vh;
  width: 100vw;
  overflow: hidden;
}
</style>
