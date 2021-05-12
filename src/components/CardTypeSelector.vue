<template>
  <div>
    <v-radio-group class="pl-4" v-model="c_type" column>
      <v-radio label="Random" color="purple darken-3" value="random"></v-radio>
      <v-radio
        class="pt-1"
        v-for="type in card_types"
        :key="type.value"
        :label="type.label"
        :color="type.colour"
        :value="type.value"
      ></v-radio>
    </v-radio-group>
  </div>
</template>


<script>
import { get_card_types } from "../api";
export default {
  name: "CardTypeSelector",
  props: {
    card_type: String,
  },
  data() {
    return {
      c_type: "random",
      card_types: [],
    };
  },
  watch: {
    c_type() {
      this.$emit("update:card_type", this.c_type);
    },
  },
  mounted() {
    this.card_types = get_card_types();
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
