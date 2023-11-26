[![License](https://img.shields.io/badge/License-Apache2-blue.svg)](https://www.apache.org/licenses/LICENSE-2.0) [![Community](https://img.shields.io/badge/Join-Community-blue)](https://developer.ibm.com/callforcode/solutions/projects/get-started/)

# Replace this heading with your team/submission name

- [Project summary](#project-summary)
  - [Overview](#overview)
  - [Objectives](#objectives)
  - [Key Features](#key-Features)
- [Technology implementation](#technology-implementation)
  - [IBM AI service(s) used](#ibm-ai-services-used)
  - [Other IBM technology used](#other-ibm-technology-used)
  - [Solution architecture](#solution-architecture)
- [Additional details](#additional-details)
  - [How to run the project](#how-to-run-the-project)
  - [Live demo](#live-demo)
- [About this project](#about-this-template)
  - [Contributing](#contributing)
  - [Versioning](#versioning)
  - [Authors](#authors)
  - [License](#license)
  - [Acknowledgments](#acknowledgments)

---
## Project summary

### Overview

Netcon is a Windows-based system designed to address the manual and tedious task of reconfiguring devices experiencing network issues at the airport. Developed during my internship JKIA's IT department, Netcon aims to automate the detection and resolution of common network problems, enhancing efficiency and reducing the workload associated with manual interventions.

### Objectives

- Automation of Device Reconfiguration: Netcon automates the process of detecting and reconfiguring devices that encounter network issues, such as unidentified networks or disconnection.

- Email Notification System: In addition to resolving issues, Netcon sends email notifications to the ICT office, providing details about the identified problem and the new configuration parameters applied.

### Key Features
- Automatic Issue Detection: Netcon autonomously identifies common network problems, eliminating the need for manual intervention.
- Configuration Parameter Updates: Devices are reconfigured with updated parameters to restore seamless network connectivity.
- Email Notifications: Netcon sends real-time email notifications to the ICT office, facilitating prompt awareness and action.

More detail is available in our [description document](./docs/DESCRIPTION.md).

## Technology implementation

### stack
- Python 3.8
- Email
- Windows batch
### Other systems used
- Windows Task Scheduler
- Command Prompt

### Solution architecture

Diagram and step-by-step description of the flow of our solution:

![Video transcription/translaftion app](https://developer.ibm.com/developer/tutorials/cfc-starter-kit-speech-to-text-app-example/images/cfc-covid19-remote-education-diagram-2.png)

## Additional details

### [How to run the project ](./docs/Netcon Setup.pdf)
To Run the project you need to Create tasks in **Task Scheduler** to detect network changes.

**Network disconnected**

- Trigger - Network profile 10001
- Run con-net
  
**Network Connected**
  
- Trigger - Network profile 10000
- Condition - Networks
- Run setuping
  
**Network state change**
  
- Trigger - Network profile 4004
- Condition - unidentified network
- Run setuping
  
---

## About this template

### Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

### Authors

<a href="https://github.com/lewiskimaru/Netcon/contributors">
  <img src="https://contributors-img.web.app/image?repo=Netcon" />
</a>

### License

This project is licensed under the Apache 2 License - see the [LICENSE](LICENSE) file for details.

### Acknowledgments

- Based on [Billie Thompson's README template](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2).
