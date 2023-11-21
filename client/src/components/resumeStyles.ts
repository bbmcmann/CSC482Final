import { StyleSheet } from "@react-pdf/renderer";

// TODO - add more variants
export const variant1 = StyleSheet.create({
  viewer: {
    width: "60vw",
    height: window.innerHeight,
  },
  page: {
    flexDirection: "row",
    backgroundColor: "#E4E4E4",
  },
  section: {
    margin: 10,
    padding: 10,
    flexGrow: 1,
  },
});
