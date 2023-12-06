import { StyleSheet } from "@react-pdf/renderer";
import random from "random";

// TODO - add more variants
const fontFamilies = {
  // TODO set font sizes
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

export const getVariantStd = () => {
  // select random font
  const font: FontFamilies =
    random.choice(["Times New Roman", "Helvetica", "Courier"]) ||
    "Times New Roman";
  const fonts = fontFamilies[font];

  // select random header color
  const headerColor = random.choice(colors) || "#000000";

  // randomize capitalization
  const capitalize = random.float() > 0.5 ? "uppercase" : undefined;

  return StyleSheet.create({
    viewer: {
      width: "60vw",
      height: "800px",
    },
    page: {
      fontFamily: fonts.Regular,
      alignItems: "center",
      marginTop: 20,
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
      width: "85%",
      marginTop: 15,
    },
    sectionTitle: {
      fontFamily: fonts.Bold,
      fontSize: fonts.sizes.title,
      borderBottom: random.float() > 0.7 ? "1px solid " + headerColor : "none",
      color: headerColor,
      textTransform: capitalize,
    },
    sectionSubTitle: {
      fontFamily: fonts.Bold,
      fontSize: fonts.sizes.text,
      marginTop: 5,
      marginLeft: 10,
    },
    sectionContent: {
      marginTop: 5,
    },
    sectionContentText: {
      fontFamily: fonts.Regular,
      fontSize: fonts.sizes.text,
      marginTop: 2,
      marginLeft: 10,
    },
    rowPrim: {
      flexDirection: "row",
      justifyContent: "space-between",
      fontSize: fonts.sizes.subTitle,
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
      fontSize: fonts.sizes.text,
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
