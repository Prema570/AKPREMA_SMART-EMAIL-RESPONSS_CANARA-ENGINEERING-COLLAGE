import java.util.Scanner;

public class Response {

    // Method to generate a professional email response
    public static String generateEmailResponse(ClientInfo clientInfo) {
        // Extract client details
        String firstName = clientInfo.getFirstName();
        String lastName = clientInfo.getLastName();
        clientInfo.getEmail();
        String country = clientInfo.getCountry();
        String location = clientInfo.getLocation();
        String language = clientInfo.getLanguage();
        String projectType = clientInfo.getProjectType();
        String serviceCategory = clientInfo.getServiceCategory();
        String website = clientInfo.getWebsite();
        String additionalInfo = clientInfo.getAdditionalInfo();

        // Generate the email content
        String emailSubject = projectType + " Development Inquiry";
        String emailBody = String.format(
                "Subject: %s\n\n" +
                        "Dear %s %s,\n\n" +
                        "Thank you for reaching out to us regarding your %s project under the %s category.\n\n" +
                        "Based on the details provided:\n" +
                        "- Project Type: %s\n" +
                        "- Service Category: %s\n" +
                        "- Location: %s, %s\n" +
                        "- Language Preference: %s\n" +
                        "- Website: %s\n\n" +
                        "Here's a brief summary of the requirements you’ve shared:\n" +
                        "%s\n\n" +
                        "We are confident in delivering a tailored solution that meets your expectations. " +
                        "Your estimated budget of $100,000 will guide us in ensuring the functionality aligns perfectly with your goals.\n\n"
                        +
                        "Please let us know if you'd like to arrange a meeting or further discuss the project details. "
                        +
                        "We are happy to clarify any aspects or make adjustments as needed.\n\n" +
                        "Looking forward to your response.\n\n" +
                        "Best regards,\n" +
                        "[Your Name]\n" +
                        "[Your Position]\n" +
                        "[Your Company Name]\n" +
                        "[Contact Information]",
                emailSubject, firstName, lastName, projectType, serviceCategory, projectType, serviceCategory,
                location, country, language, (website.equalsIgnoreCase("none") ? "No website provided" : website),
                additionalInfo);

        return emailBody;
    }

    public static void main(String[] args) {
        // Create a Scanner object for input
        Scanner scanner = new Scanner(System.in);

        // Gather client information
        System.out.println("Please provide the following client details to generate a response:");

        System.out.print("Client First Name: ");
        String firstName = scanner.nextLine().trim();

        System.out.print("Client Last Name: ");
        String lastName = scanner.nextLine().trim();

        System.out.print("Client Email: ");
        String email = scanner.nextLine().trim();

        System.out.print("Client Country: ");
        String country = scanner.nextLine().trim();

        System.out.print("Client Location (if provided): ");
        String location = scanner.nextLine().trim();
        if (location.isEmpty())
            location = "Not provided";

        System.out.print("Client Language: ");
        String language = scanner.nextLine().trim();

        System.out.print("Project Type: ");
        String projectType = scanner.nextLine().trim();

        System.out.print("Service Category: ");
        String serviceCategory = scanner.nextLine().trim();

        System.out.print("Client Website (if any): ");
        String website = scanner.nextLine().trim();
        if (website.isEmpty())
            website = "None";

        System.out.print("Additional Information (if any): ");
        String additionalInfo = scanner.nextLine().trim();
        if (additionalInfo.isEmpty())
            additionalInfo = "No additional information provided.";

        // Create a ClientInfo object with the gathered information
        ClientInfo clientInfo = new ClientInfo(firstName, lastName, email, country, location, language,
                projectType, serviceCategory, website, additionalInfo);

        // Generate the email response
        String emailResponse = generateEmailResponse(clientInfo);

        // Output the response
        System.out.println("\nGenerated Email Response:");
        System.out.println(emailResponse);

        scanner.close();
    }
}

// ClientInfo class to store the client details
class ClientInfo {
    private String firstName, lastName, email, country, location, language, projectType, serviceCategory, website,
            additionalInfo;

    public ClientInfo(String firstName, String lastName, String email, String country, String location, String language,
            String projectType, String serviceCategory, String website, String additionalInfo) {
        this.firstName = firstName;
        this.lastName = lastName;
        this.email = email;
        this.country = country;
        this.location = location;
        this.language = language;
        this.projectType = projectType;
        this.serviceCategory = serviceCategory;
        this.website = website;
        this.additionalInfo = additionalInfo;
    }

    public String getFirstName() {
        return firstName;
    }

    public String getLastName() {
        return lastName;
    }

    public String getEmail() {
        return email;
    }

    public String getCountry() {
        return country;
    }

    public String getLocation() {
        return location;
    }

    public String getLanguage() {
        return language;
    }

    public String getProjectType() {
        return projectType;
    }

    public String getServiceCategory() {
        return serviceCategory;
    }

    public String getWebsite() {
        return website;
    }

    public String getAdditionalInfo() {
        return additionalInfo;
    }
}
