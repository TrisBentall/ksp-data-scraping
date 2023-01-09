<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/TrisBentall/ksp-data-scraping">
<!--    <img src="images/logo.png" alt="Logo" width="80" height="80"> -->
  </a>

<h3 align="center">KSP Data Scraping</h3>

  <p align="center">
    A tool to scrape Kerbal Space Program engine part data from its gamefiles
    <br />
    <a href="https://github.com/TrisBentall/ksp-data-scraping"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/TrisBentall/ksp-data-scraping/issues">Report Bug</a>
    ·
    <a href="https://github.com/TrisBentall/ksp-data-scraping/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

This is a small python project that aims to scrape part data from the Kerbal Space Program gamefiles, for use in data analysis and payload calculations.


<!-- GETTING STARTED -->
## Getting Started

This is a rough guide on how to use the scripts, a full guide will be coming soon once there has been a full release. Use at your own discretion.

### Prerequisites

Python3 is required to run.
These packages will also be required.
* os
* csv
* pandas

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/TrisBentall/ksp-data-scraping.git
   ```
2. Install the required packages
   ```py
   pip install os csv pandas
   ```
3. In the python script, replace YOURPATH with the file path to your gamedata
   ```py
   Path = 'YOURPATH'
   ```




<!-- USAGE EXAMPLES 
## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_

<p align="right">(<a href="#readme-top">back to top</a>)</p>
-->


<!-- ROADMAP -->
## Roadmap

There are numerous features I'd like to add to this in the future, these are not garranteed and there is no timeline on when they might be added

- Split engine data to display its performance in different conditions, e.g. show how the R.A.P.I.E.R engine performs when in its air breathing configuration vs in its closed cycle configuration
- Allow certain statistics to be graphed, and compared to other engines
- Deliver a fully functional GUI

If you have any feature requests, please feel free to create an issue and I'll look at adding it into the roadmap.

See the [open issues](https://github.com/TrisBentall/ksp-data-scraping/issues) for a full list of proposed features (and known issues).




<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request




<!-- LICENSE -->
## License

Distributed under the GPL-3.0 License. See `LICENSE.txt` for more information.




<!-- CONTACT -->
## Contact

Tris Bentall - [@trisbentall](https://twitter.com/trisbentall)

Project Link: [https://github.com/TrisBentall/ksp-data-scraping](https://github.com/TrisBentall/ksp-data-scraping)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
<!--
## Acknowledgments

* []()
* []()
* []()

<p align="right">(<a href="#readme-top">back to top</a>)</p>
-->


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/TrisBentall/ksp-data-scraping.svg?style=for-the-badge
[contributors-url]: https://github.com/TrisBentall/ksp-data-scraping/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/TrisBentall/ksp-data-scraping.svg?style=for-the-badge
[forks-url]: https://github.com/TrisBentall/ksp-data-scraping/network/members
[stars-shield]: https://img.shields.io/github/stars/TrisBentall/ksp-data-scraping.svg?style=for-the-badge
[stars-url]: https://github.com/TrisBentall/ksp-data-scraping/stargazers
[issues-shield]: https://img.shields.io/github/issues/TrisBentall/ksp-data-scraping.svg?style=for-the-badge
[issues-url]: https://github.com/TrisBentall/ksp-data-scraping/issues
[license-shield]: https://img.shields.io/github/license/TrisBentall/ksp-data-scraping.svg?style=for-the-badge
[license-url]: https://github.com/TrisBentall/ksp-data-scraping/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/trisbentall
[product-screenshot]: images/screenshot.png