<template>
  <div class="hello">
    <v-card class="mx-auto" max-width="800" outlined>
      <v-list-item three-line>
        <v-list-item-content>
          <div class="overline mb-4">Random Card</div>
          <v-card-text>
            <v-container fluid>
              <v-row>
                <v-col cols="12" sm="6" md="6">
                  <v-radio-group v-model="card_type" column>
                    <v-radio
                      label="Random"
                      color="purple darken-3"
                      value="all"
                    ></v-radio>
                    <v-radio
                      label="Data Head"
                      color="red darken-3"
                      value="data_head"
                    ></v-radio>
                    <v-radio
                      label="Star Performer"
                      color="green darken-3"
                      value="star_performer"
                    ></v-radio>
                    <v-radio
                      label="Creative Cat"
                      color="blue darken-3"
                      value="creative_cat"
                    ></v-radio>
                    <v-radio
                      label="Word Worm"
                      color="yellow darken-3"
                      value="worm_worm"
                    ></v-radio>
                  </v-radio-group>
                </v-col>
              </v-row>
            </v-container>
          </v-card-text>
          <v-list-item-title color="green" class="headline mb-1">
            {{ card.card_game }}
          </v-list-item-title>
          <v-list-item-subtitle>{{ card.game_info }}</v-list-item-subtitle>
          <v-card-text>
            {{ card.game_text }}
          </v-card-text>
          <v-btn
            rounded
            color="green"
            max-width="150"
            @click="show_answer = !show_answer"
            >Show Answer</v-btn
          >
          <v-card-text v-if="show_answer">
            {{ card.answer }}
          </v-card-text>
        </v-list-item-content>
      </v-list-item>

      <v-card-actions>
        <v-btn color="primary" @click="get_random_card">
          Get Random Card
        </v-btn>
      </v-card-actions>
    </v-card>
  </div>
</template>

<script>
import cardData from "../data/song_cards.json";
import _ from "lodash";
export default {
  name: "HelloWorld",
  props: {
    msg: String,
  },
  data() {
    return {
      card_data: cardData,
      card: {},
      show_answer: false,
      card_type: "all",
      // TODO: define card types as an enum
      //        define card games as enums
    };
  },
  methods: {
    get_random_card: function () {
      // have the card game enum sample the data

      this.card = _.sample(this.card_data);
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
