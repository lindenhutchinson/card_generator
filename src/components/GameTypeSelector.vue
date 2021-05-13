<template>
  <div>
    <v-radio-group class="pl-4" v-model="g_type">
      <v-radio label="Random" color="purple darken-3" value="random"></v-radio>
      <v-radio
        class="pt-1"
        v-for="game in games"
        :key="game.value"
        :label="game.label"
        :color="game_color"
        :value="game.value"
      ></v-radio>
    </v-radio-group>
  </div>
</template>


<script>
import { get_game_types, get_card_types } from "../api";
export default {
  name: "GameTypeSelector",
  props: {
    game_type: String,
    card_type: String,
  },
  data() {
    return {
      game_types: [],
      card_types: [],
      g_type: "random",
    };
  },
  computed: {
    games: function () {
      return this.game_types[this.card_type];
    },
    game_color: function () {
      return this.card_types[this.card_type].colour;
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
  mounted() {
    this.game_types = get_game_types();
    this.card_types = get_card_types();
  },
};
</script>
