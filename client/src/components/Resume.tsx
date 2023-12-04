import {
  Document,
  Link,
  PDFViewer,
  Page,
  Text,
  View,
} from "@react-pdf/renderer";
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
    description: string[];
  }[];
  skills: string[];
};

export default function Resume(props: ResumeProps) {
  // TODO: Add a button to switch between variants
  const styles = variant1;

  return (
    <div>
      <h3>Resume</h3>
      <PDFViewer style={styles.viewer}>
        <Document title={`${props.name} Resume`}>
          <Page size="A4" style={styles.page}>
            <View style={styles.header}>
              <Text style={styles.name}>{props.name}</Text>
              <View style={styles.headerline}>
                <Text style={styles.contact}>
                  <Link src="https://www.google.com/">{props.email}</Link>
                </Text>
                <Text style={styles.contact}>{props.phone}</Text>
                <Text style={styles.contact}>
                  <Link src="https://www.google.com/">{props.linkedin}</Link>
                </Text>
              </View>
            </View>
            <View style={styles.section}>
              <Text style={styles.sectionTitle}>Education</Text>
              <View style={styles.sectionContent}>
                <View style={styles.rowPrim}>
                  <Text style={styles.sectionContentText}>
                    {props.education.school}
                  </Text>
                  <Text style={styles.sectionContentText}>
                    {props.education.location}
                  </Text>
                </View>
                <View style={styles.rowSec}>
                  <Text style={styles.sectionContentText}>
                    {props.education.degree}
                  </Text>
                  <Text style={styles.sectionContentText}>
                    {props.education.start} - {props.education.end}
                  </Text>
                </View>
                {props.education.gpa > 3.0 ? (
                  <Text style={styles.sectionContentText}>
                    GPA: {props.education.gpa}
                  </Text>
                ) : null}
                <Text style={styles.sectionContentText}>
                  Relevant Courses: {props.education.courses.join(", ")}
                </Text>
              </View>
            </View>
            <View style={styles.section}>
              <Text style={styles.sectionTitle}>Experience</Text>
              <View style={styles.sectionContent}>
                {props.experience.map((exp) => (
                  <View
                    key={exp.company + exp.start}
                    style={styles.experienceSection}
                  >
                    <View style={styles.rowPrim}>
                      <Text style={styles.sectionContentText}>
                        {exp.company}
                      </Text>
                      <Text style={styles.sectionContentText}>
                        {exp.location}
                      </Text>
                    </View>
                    <View style={styles.rowSec}>
                      <Text style={styles.sectionContentText}>
                        {exp.position}
                      </Text>
                      <Text style={styles.sectionContentText}>
                        {exp.start} - {exp.end}
                      </Text>
                    </View>
                    {exp.description.map((desc, i) => (
                      <Text key={i} style={styles.bulletPoint}>
                        • {desc}
                      </Text>
                    ))}
                  </View>
                ))}
              </View>
            </View>
            <View style={styles.section}>
              <Text style={styles.sectionTitle}>
                Projects/Outside Experience
              </Text>
              <View style={styles.sectionContent}>
                {props.projects.map((proj) => (
                  <View key={proj.role} style={styles.experienceSection}>
                    <View style={styles.rowPrim}>
                      <Text style={styles.sectionContentText}>{proj.name}</Text>
                    </View>
                    <View style={styles.rowSec}>
                      <Text style={styles.sectionContentText}>{proj.role}</Text>
                      <Text style={styles.sectionContentText}>
                        {proj.start} - {proj.end}
                      </Text>
                    </View>
                    {proj.description.map((desc, i) => (
                      <Text key={i} style={styles.bulletPoint}>
                        • {desc}
                      </Text>
                    ))}
                  </View>
                ))}
              </View>
            </View>
            <View style={styles.section}>
              <Text style={styles.sectionTitle}>Skills</Text>
              <View style={styles.sectionContent}>
                <Text style={styles.sectionContentText}>
                  {props.skills.join(", ")}
                </Text>
              </View>
            </View>
          </Page>
        </Document>
      </PDFViewer>
    </div>
  );
}
