// Import React
import React from "react";

// Import Spectacle Core tags
import {
  Appear,
  BlockQuote,
  Cite,
  CodePane,
  Deck,
  Fill,
  Heading,
  Image,
  Layout,
  Link,
  ListItem,
  List,
  Markdown,
  Quote,
  Slide,
  Spectacle,
  Text
} from "spectacle";

import CodeSlide from 'spectacle-code-slide';
const code = require('./filterFilter');

// Import image preloader util
import preloader from "spectacle/lib/utils/preloader";

// Import theme
import createTheme from "spectacle/lib/themes/default";

// Import custom component
import Interactive from "../assets/interactive";

// Require CSS
require("normalize.css");
require("spectacle/lib/themes/default/index.css");


const images = {
  city: require("../assets/city.jpg"),
  kat: require("../assets/kat.png"),
  logo: require("../assets/formidable-logo.svg"),
  markdown: require("../assets/markdown.png")
};

preloader(images);

const theme = createTheme({
  primary: "#ff4081"
});

export default class Presentation extends React.Component {
  render() {
    return (
      <Spectacle theme={theme}>
        <Deck transition={["zoom", "slide"]} transitionDuration={500}>
          <Slide transition={["zoom", "fade"]} bgColor="primary" notes="<ul><li>talk about that</li><li>and that</li></ul>">
            <Heading size={1} fit caps lineHeight={1} textColor="black">
              filterFilter in Angular 1.2!
            </Heading>
          </Slide>
          <CodeSlide transition={[]} lang="js" code={code} ranges={[
            { loc: [ 0, 15]},
            { loc: [ 1,  2], note: '3 params, array & expression & comparator' },
            { loc: [95, 103], note: 'the end of filterFilter' },
            { loc: [ 7, 15], note: 'what are check doing?' },
            { loc: [83, 86], note: 'where are predicates from?' },
            { loc: [89, 92], note: 'where are predicates from?' },
            { loc: [71, 86], note: 'process of param expression' },
            { loc: [72, 79], note: 'Set up expression object and fall through' },
            { loc: [78, 89], note: 'Set up predicates for object' },
            { loc: [38, 54], note: 'search function' },
            { loc: [39, 42], note: 'usage of \'!\' before search string' },
            { loc: [43, 51], note: 'use comparator to comparing' },
            { loc: [51, 58], note: 'Scenario of $.keyword' },
            { loc: [60, 67], note: 'Scenario of array in object' },
            { loc: [16, 30], note: 'adapt comparator to function' },
            { loc: [17, 21], note: 'comparator of boolean' },
            { loc: [22, 35], note: 'comparator of obj & string' },
          ]}/>
          <Slide transition={["zoom", "fade"]} bgColor="primary" notes="<ul><li>talk about that</li><li>and that</li></ul>">
            <Heading size={1} fit caps lineHeight={1} textColor="black">
              Thanks!
            </Heading>
          </Slide>
        </Deck>
      </Spectacle>
    );
  }
}
