import { Document, PDFViewer, Page, Text, View } from "@react-pdf/renderer";
import { variant1 } from "./resumeStyles";

export type ResumeProps = {
  name: string;
  email: string;
  phone: string;
  linkedin: string;
  education: {
    school: string;
    location: string;
    degree: string;
    gpa: number;
    start: string;
    end: string;
    courses: string[];
  };
  experience: {
    company: string;
    location: string;
    position: string;
    start: string;
    end: string;
    description: string[];
  }[];
  projects: {
    name: string;
    role: string;
    start: string;
    end: string;
    description: string;
  }[];
  skills: string[];
};

export default function Resume(props: ResumeProps) {
  // TODO: Add a button to switch between variants
  const styles = variant1;

  console.log(props);
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
