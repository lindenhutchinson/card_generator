<template>
  <div>
    <v-radio-group v-model="g_type">
      <v-radio label="Random" color="purple darken-3" value="random"></v-radio>

      <v-radio
        v-for="game in games"
        :key="game.value"
        :label="game.label"
        :color="game.colour"
        :value="game.value"
      ></v-radio>
    </v-radio-group>
  </div>
</template>


<script>
import { game_types } from "../api";
export default {
  name: "GameTypeSelector",
  props: {
    game_type: String,
    card_type: String,
  },
  data() {
    return {
      game_types: game_types,
      g_type: "random",
    };
  },
  computed: {
    games: function () {
      return this.game_types[this.card_type];
    },
  },
  watch: {
    card_type() {
      this.g_type = "random";
    },
    g_type() {
      this.$emit("update:game_type", this.g_type);
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
