import { Document, PDFViewer, Page, Text, View } from "@react-pdf/renderer";
import { variant1 } from "./resumeStyles";

export default function Resume() {
  // TODO: Add a button to switch between variants
  const styles = variant1;

  return (
    <div>
      <h3>Resume</h3>
      <PDFViewer style={styles.viewer}>
        <Document>
          <Page size="A4" style={styles.page}>
            <View style={styles.section}>
              <Text>Section #1</Text>
            </View>
            <View style={styles.section}>
              <Text>Section #2</Text>
            </View>
          </Page>
        </Document>
      </PDFViewer>
    </div>
  );
}
