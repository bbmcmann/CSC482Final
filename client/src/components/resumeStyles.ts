import { StyleSheet } from "@react-pdf/renderer";

// TODO - add more variants
export const variant1 = StyleSheet.create({
  viewer: {
    width: "60vw",
    height: "800px",
  },
  page: {
    fontFamily: "Times-Roman",
    alignItems: "center",
    marginTop: 20,
  },
  header: {
    width: "85%",
    alignItems: "center",
    paddingBottom: 5,
  },
  name: {
    fontFamily: "Times-Bold",
    fontSize: 30,
  },
  headerline: {
    flexDirection: "row",
  },
  contact: {
    fontSize: 12,
    marginLeft: 10,
  },
  section: {
    width: "85%",
    marginTop: 15,
  },
  sectionTitle: {
    fontFamily: "Times-Bold",
    fontSize: 18,
    borderBottom: "1px solid black",
  },
  sectionContent: {
    marginTop: 5,
  },
  sectionContentText: {
    fontSize: 12,
    marginTop: 2,
    marginLeft: 10,
  },
  rowPrim: {
    flexDirection: "row",
    justifyContent: "space-between",
    fontFamily: "Times-Bold",
    fontSize: 14,
  },
  rowSec: {
    flexDirection: "row",
    justifyContent: "space-between",
    fontFamily: "Times-Italic",
  },
  experienceSection: {
    marginBottom: 5,
  },
  bulletPoint: {
    fontSize: 12,
    marginLeft: 10,
    marginTop: 1.5,
  },
});
