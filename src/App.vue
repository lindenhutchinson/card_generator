<template>
  <v-app>
    <v-app-bar app color="primary" dark>
      <div class="align-center">
        <v-spacer></v-spacer>
        <v-card-title class="font-weight-medium"
          >Random Card Generator</v-card-title
        >
        <v-spacer></v-spacer>
      </div>

      <v-spacer></v-spacer>
    </v-app-bar>

    <v-main>
      <Home />
    </v-main>
  </v-app>
</template>

<script>
import Home from "./components/Home";

export default {
  name: "App",

  components: {
    Home,
  },

  data: () => ({
    //
  }),
};
</script>

