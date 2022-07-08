---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.13.8
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

# Books, Papers, and Online Mterials
You can download the ebooks from our library. 
## EM Methods
- Finite Difference Time Domain (FDTD)
    - **`Slides`** [A introduction to Meep and FDTD](http://ab-initio.mit.edu/~ardavan/stuff/IEEE_Photonics_Society_SCV3.pdf)
    - **`Books`** [Introduction to the finite-difference time-domain (FDTD) method for electromagnetics](https://ieeexplore.ieee.org/document/6812520)
    - **`Book`** [Advances in FDTD Computational Electrodynamics: Photonics and Nanotechnology](http://ieeexplore.ieee.org/document/9100982)
    - **`software`** [Meep](https://meep.readthedocs.io/): electromagnetics simulation using FDTD. Python interface. **MPI**  parallelism, **Bloch** boundary, **GDSII** support 
    - **`software`** [gprMax](https://www.gprmax.com/): electromagnetics simulation using FDTD. Python interface. **GPU**, but currently less supports for photonics such as periodic boundary conditions  
- Boundary element method (BEM)
    - **`paper`** Retarded field calculation of electron energy loss in inhomogeneous dielectrics, [Phys. Rev. B 65, 115418 (2002)](https://journals.aps.org/prb/abstract/10.1103/PhysRevB.65.115418)
    - **`software`** [MNPBEM toolbox](https://homepage.uni-graz.at/de/ulrich.hohenester/software/) BEM methods using Matlab
    **`paper`** [MNPBEM – A Matlab toolbox for the simulation of plasmonic nanoparticles](https://doi.org/10.1016/j.cpc.2011.09.009)
    - **`paper`** [Universal analytical modeling of plasmonic nanoparticles](https://doi.org/10.1039/C6CS00919K)
    - **`paper`** [Modelling the optical response of gold nanoparticles](https://pubs.rsc.org/en/content/articlehtml/2008/cs/b711486a)
    - **`software`** [Scuff-EM](http://homerreid.github.io/scuff-em-documentation/) inactivate **`Slides`** [Integral-equation approaches](https://homerreid.github.io/SCUFFEMTutorialSymposium/IntegralEquations/)
    -**`paper`** [Generalized Taylor–Duffy Method for Efficient Evaluation of Galerkin Integrals in Boundary-Element Method Computations](https://doi.org/10.1109/TAP.2014.2367492)
- Rigorous coupled-wave analysis, transfer matrix method
    - **`Software`** [S4](https://web.stanford.edu/group/fan/S4/index.html): An RCWA solver by Stanford's group. However, it is not activately maintained now, and the installation method from the original site seems not working. Follow the method at [Rayflare](https://rayflare.readthedocs.io/en/latest/)
    
    
- Anaytical methods
   - Mie thoey: analytic solutions for spheres 
     - **`Book`** [Absorption and scattering of light by small particles](https://onlinelibrary.wiley.com/doi/book/10.1002/9783527618156)
     - **`Article`** [The Extension of Mie Theory to Multiple Spheres](https://onlinelibrary.wiley.com/doi/book/10.1002/9783527618156)
   - Waveguides
     - **`Book`** [Otical waveguide theory](https://link.springer.com/book/10.1007/978-1-4613-2813-1); **`Chapter`** Waveguides with exact solutions
   - Dipole raditation in a planar structure
     - **`Book `** Lateral Electromagnetic Waves by King and Wu: discussions about dipole radiation above a plane using the Sommerfeld integrals. The book has the most complete formulas of the various `Sommerfeld integrals`
      - **`Book`** Dyadic Green Functions in Electromagnetic Theory by Chen-To Tai: using the  Dyadic Green Functions in various coordinate systems. **`Chapter 11`** planar structures.
     - **`Book`** Principles of Nano-Optics **`Chpaters 2, 3`** Dyadic green functions
   - Advanced Electromagnetism 
     - **`Book`** Classical Electrodynamics by John David Jackson
     - **`Book`** Modern Electrodynamics by Andre Zangwill 
   
## Photonic Crystals
- **`Tutorial`** [Five lectures of photonic crystals by Steven G. Johnson](http://ab-initio.mit.edu/photons/tutorial/)
- **`Book`** [Photonic Crystals: Molding the Flow of Light (second edition)](http://ab-initio.mit.edu/book/photonic-crystals-book.pdf) 

## Plasmonics 
- **`paper`** [The spaser as a nanoscale quantum generator and ultrafast amplifier](https://iopscience.iop.org/article/10.1088/2040-8978/12/2/024004)
- **`Book`** [Principles of Nano-Optics](https://www.cambridge.org/core/books/principles-of-nanooptics/E884E5F4AA76DF179A1ECFDF77436452)
- **`Book`** [Nano and Quantum Optics: An Introduction to Basic Principles and Theory](https://link.springer.com/book/10.1007/978-3-030-30504-8)
- **`pdf`** [物理雙月刊：金屬表面電漿簡介](https://jhihsheng.github.io/Ref/pdf/physics_bimonth_intro_SPP.pdf)
- **`pdf`** [物理雙月刊：表面電漿理論與模擬](https://jhihsheng.github.io/Ref/pdf/physics_bimonth_Theory_Simulation_SPP.pdf)
- **`Slides`** [Nanoplasmonics: Citius, Minimius, Fortius! (Faster, Smaller, Stronger!)](http://physics.gsu.edu/stockman/data/Smaller_Stronger_Faster_40_min.pdf)
- **`Slides`** [Nanoplasmonics Fundamentals and Applications](http://physics.gsu.edu/stockman/data/Nanoplasmonics_Fundamentals_and_Applications_Erice_2017_200_min.pdf)
- **`Article`** [用光控制光：以奈米材料大幅增強光學非線性](https://pb.ps-taiwan.org/modules/news/article.php?storyid=645)
- **`Article`** [奈米光學饗宴─散射式近場光學顯微鏡 ](https://pb.ps-taiwan.org/modules/news/article.php?storyid=634)