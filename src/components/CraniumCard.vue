<template>
  <v-card
    style="margin: 0 auto"
    v-if="card.card_type"
    class="mx-auto card pb-2"
    :class="card.card_type.value"
    outlined
    raised
  >
    <v-list-item three-line>
      <v-list-item-content>
        <v-card-title class="headline card-title pl-2 pb-5 pt-2">{{
          card.game_type
        }}</v-card-title>

        <v-card flat class="card-text pt-2">
          <div v-if="typeof card.game_text === 'string'">
            <v-card-subtitle>
              <b>{{ card.game_text }}</b>
            </v-card-subtitle>
          </div>
          <div v-else>
            <div>
              <v-card-subtitle>
                <b>{{ card.game_text[0] }}</b>
              </v-card-subtitle>
            </div>
            <v-card-subtitle class="pb-0 pt-0" v-for="txt in card.game_text.slice(1)" v-bind:key="txt">
              {{ txt }}
            </v-card-subtitle>
          </div>
          <v-card-text class="pb-10">{{ card.game_info }}</v-card-text>
          <v-expand-transition>
            <v-card
              raised
              justify="center"
              class="card-text v-card--reveal"
              v-if="show_answer"
            >
              <div
                v-if="typeof card.answer === 'string'"
                class="answer-text pt-15"
              >
                <p>{{ card.answer }}</p>
              </div>
              <div v-else class="answer-text pt-15">
                <p v-for="a in card.answer" v-bind:key="a">{{ a }}</p>
              </div>
              
            </v-card>
          </v-expand-transition>
          <v-btn color="grey lighten-3" block v-if="!show_answer" @click="show_answer = true">Show Answer</v-btn>
          <v-btn color="grey lighten-3" v-else block @click="show_answer = false">Close</v-btn>
              
        </v-card>
      </v-list-item-content>
    </v-list-item>
  </v-card>
</template>



<script>
export default {
  name: "CraniumCard",
  props: {
    card: {
      game_text: String,
      answer: String,
      game_type: String,
      game_info: String,
      card_type: String,
    },
  },
  data() {
    return {
      show_answer: false,
    };
  },
  watch: {
    card: function () {
      this.show_answer = false;
    },
  },
};
</script>
<style scoped lang="scss">
@import "../styles/index.scss";
</style>