
This repository is made to understand asymmetric cryptography (in this case RSA) and how to generate public and private Keys given two prime numbers and a public exponent.

A list of commonly used resources that I find helpful are listed in the acknowledgements.

### Built With
This section should list any major frameworks that you built your project using. Leave any add-ons/plugins for the acknowledgements section. Here are a few examples.
* [PYTHON3](https://python.org)
* [JETBRAINS PYCHARM](https://jetbrains.com)


<!-- GETTING STARTED -->
## Getting Started

Follow the provided instructions in this readme file to use RSAfromscratch.
To get a local copy up and running follow these simple example steps.

### Prerequisites

Use the Windows/Linux/IDE terminal and pip subsequently to install the requirements.txt list of modules.
* cryptodome
```sh
pip install -r requirements.txt
```

### Installation

1. Clone the repo
```sh
git clone https://github.com/gasparllamazares/RSAfromscratch.git
```
4. Execute `main.py`
```sh
python3 main.py
```



<!-- USAGE EXAMPLES -->
## Usage

The program comes with it's own "menu", now only supports key generation and export.

_For more examples, please refer to the [Documentation](https://example.com)_



<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/gasparllamazares/RSAfromscratch/issues) for a list of proposed features (and known issues).

* def fast_exp()

Decrypts a number given c, d, n, and it's used to make a quick check of the integrity of the parameters.


* def euclidean(phi, e):

Generates our private exponent by calculating the inverse of the public exponent using the Extended Euclidean Algorithm.


* def generate(): 

Generates (given a initial number of bytes of the desired key), two prime numbers (p, q), then the modulus n (p x q), phi Φ = (p-1)(q-1).

Defines public exponent (e) 65537 (fixed).

Checks that the public exponent is not a factor of Φ (Φ mod e != 0).

Uses euclidean() function to obtain d (private exponent)

Checks the integrity of n, e, d by encrypting a random number m and decrypting it.

c = (m^e) mod (n)

Gives the option to store the keys in a text file.








<!-- CONTRIBUTING -->
## Contributing

Contributions are allways **greatly appreciated** and also any aproach for this program in C++ could result helpfull for me.
To contribute: 

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

NO LICENSE AT ALL



<!-- CONTACT -->
## Contact

Twitter - [@gasparllamazar3](https://twitter.com/gasparllamazar3) 
Instagram - [@gasparllamazares](https://instagram.com/gasparllamazares)

Project Link: [https://github.com/gasparllamazares/RSAfromscratch](https://github.com/gasparllamazares/RSAfromscratch)



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements
* [How the RSA algorithm works, including how to select d, e, n, p, q, and φ (phi)](https://www.youtube.com/watch?v=Z8M2BTscoD4)
* [Public key cryptography - Diffie-Hellman Key Exchange](https://www.youtube.com/watch?v=YEBfamv-_do)
* [Wikipedia RSA](https://es.wikipedia.org/wiki/RSA)






<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=flat-square
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=flat-square
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=flat-square
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=flat-square
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=flat-square
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: images/screenshot.png
