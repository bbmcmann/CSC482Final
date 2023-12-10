import { StyleSheet } from "@react-pdf/renderer";
import random from "random";

const fontFamilies = {
  "Times New Roman": {
    Regular: "Times-Roman",
    Bold: "Times-Bold",
    Italic: "Times-Italic",
    sizes: {
      title: 18,
      subTitle: 14,
      text: 12,
    },
  },
  Helvetica: {
    Regular: "Helvetica",
    Bold: "Helvetica-Bold",
    Italic: "Helvetica-Oblique",
    sizes: {
      title: 18,
      subTitle: 14,
      text: 12,
    },
  },
  Courier: {
    Regular: "Courier",
    Bold: "Courier-Bold",
    Italic: "Courier-Oblique",
    sizes: {
      title: 14,
      subTitle: 12,
      text: 10,
    },
  },
};

export type FontFamilies = "Times New Roman" | "Helvetica" | "Courier";

const colors = [
  "#000000",
  "#000000",
  "#000000",
  "#000000",
  "#000000",
  "#9ac8eb",
  "#a1cdce",
  "#7b92aa",
  "#37667e",
];

export const getVariantStd = (year: number, numEntries: number) => {
  // select random font
  const font: FontFamilies =
    random.choice(["Times New Roman", "Helvetica", "Courier"]) ||
    "Times New Roman";
  const fonts = fontFamilies[font];
  let fontSizeBias = (4 - year) * 1.5;
  if (font == "Courier") {
    fontSizeBias = fontSizeBias + 1;
  }

  // select random header color
  const headerColor = random.choice(colors) || "#000000";

  // randomize capitalization
  const capitalize = random.float() > 0.5 ? "uppercase" : undefined;

  // decide line height based on number of entries to fill page
  let lineHeight = 1;
  if (numEntries < 3) {
    lineHeight = 1.5;
  } else if (numEntries == 3 && year > 2) {
    lineHeight = 1.25;
  }

  return StyleSheet.create({
    viewer: {
      width: "60vw",
      height: "800px",
    },
    page: {
      fontFamily: fonts.Regular,
      alignItems: "center",
      marginTop: 15,
      lineHeight: lineHeight,
    },
    header: {
      width: "85%",
      alignItems: "center",
      paddingBottom: 5,
      color: headerColor,
    },
    name: {
      fontFamily: fonts.Bold,
      fontSize: 30,
      textTransform: capitalize,
    },
    headerline: {
      flexDirection: "row",
    },
    contact: {
      fontSize: fonts.sizes.text,
      marginLeft: 10,
    },
    section: {
      marginTop: 10,
      width: "85%",
    },
    sectionTitle: {
      fontFamily: fonts.Bold,
      fontSize: fonts.sizes.title + fontSizeBias,
      borderBottom: random.float() > 0.7 ? "1px solid " + headerColor : "none",
      color: headerColor,
      textTransform: capitalize,
    },
    sectionSubTitle: {
      fontFamily: fonts.Bold,
      fontSize: fonts.sizes.text + fontSizeBias,
      marginTop: 5,
      marginLeft: 10,
    },
    sectionContent: {
      marginTop: 5,
    },
    sectionContentText: {
      fontFamily: fonts.Regular,
      fontSize: fonts.sizes.text + fontSizeBias,
      marginTop: 2,
      marginLeft: 10,
    },
    rowPrim: {
      flexDirection: "row",
      justifyContent: "space-between",
      fontSize: fonts.sizes.subTitle + fontSizeBias,
    },
    rowSec: {
      flexDirection: "row",
      justifyContent: "space-between",
      fontFamily: fonts.Italic,
    },
    experienceSection: {
      marginBottom: 5,
    },
    bulletPoint: {
      fontSize: fonts.sizes.text + fontSizeBias,
      marginLeft: 10,
      marginTop: 1.5,
    },
    icon: {
      width: 15,
      height: 15,
      color: headerColor,
    },
  });
};
