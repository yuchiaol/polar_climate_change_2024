(python_by_example)=

# HW Linear Baroclinic Model

## Individual Work

## Credits: 15%

## Grading:
- Yu-Chiao Liang (9%)
- TA xxx (3%) 
- TA xxx (3%)

## Deadline: xxx

## The Tasks

- Set up and run the model successfully.
- Learn how to change forcing strength, shape, and location.
- Reproduce the Central Pacific forcing.
- Check:
  - Background fields.
  - Winds, sea-level pressure, geopotential height, temperature fields.
- Use diagnostic tools to analyze the wave activity features.

## The Model

This linear baroclinic model (LBM) was developed and maintained by Dr Michiya Hayashi. 
The official website is [here](https://ccsr.aori.u-tokyo.ac.jp/~lbm/sub/lbm_4.html).
I have ported LBM on workstation xxx. Please ask your group leaders for login information.

## Running the Model

1. Copy folder LBM_standard to your own directory.
2. export LNHOME='/home/xxx/LBM_xxx/ln_solver'
3. Edit Lmake.inc file
4. Compile model:
   - cd $LNHOME/model/src
   - make clean
   - make lib 
   - You should find a file called liblbm2t21ml11c.a under $LNHOME/model/lib/linux/
5. Builde model:
   - cd $LNHOME/model/src 
   - make clean.special
   - make lbm
   - You should find a file called lbm2.t21ml11ctintgr under $LNHOME/model/bin/linux
6. Prepare forcing:
   - cd $LNHOME/solver/util
   - Edit SETPAR
   - make clean
   - make
   - ./mkfrcng
   - cd $LNHOME/sample/
   - You should see the forcing file you created.
   - Use Grads to check forcing (e.g., (1) edit xxx.ctl, (2) type grads, (3) open xxx.ctr, (4) d t)
7. Run model:
   - cd $LNHOME/model/sh/tintgr
   - Edit xxx.csh (e.g., linear-run.t21l5.test.csh)
   - ./xxx.csh
   - Monitor output log file under $LNHOME/data/out
8. Postprocess and visualize results
   - cd $LNHOME/solver/util
   - Edit SETPAR
   - ./gt2gr
   - Convert grd file to nc file: cdo -f nc import_binary xxx.ctl output_temp.nc

## Tropical Forcing Example
```{figure} /_static/lecture_specific/figures/lbm_cp_forcing.gif
:scale: 40%
```
## Diagnostic Tools

- Eliassen-Palm (EP) flux
  - [NCL function](https://www.ncl.ucar.edu/Applications/EPflux.shtml)
  - [Python function](https://github.com/mjucker/aostools/blob/master/climate.py)
- Wave Activity Fluxes  
  - [GrADS](http://www.atmos.rcast.u-tokyo.ac.jp/nishii/programs/index.html)
  - [Python](https://github.com/marisolosman/Reunion_Clima/blob/master/WAF/Calculo_WAF.ipynb)
- Rossby Wave Source
  - [Python](https://ajdawson.github.io/windspharm/latest/examples/rws_standard.html) 
- Streamfunction and Velocity Potential
  - [Python](https://ajdawson.github.io/windspharm/latest/examples/sfvp_standard.html)

## References

- [Ting and Held (1990)](https://journals.ametsoc.org/view/journals/atsc/47/21/1520-0469_1990_047_2546_tswrta_2_0_co_2.xml)
- [Eliassen and Palm (1961)](https://math.nyu.edu/~pauluis/TEM/TEM/Papers_files/Ellassen%26Palm_1961.pdf)
- [Takaya and Nakamura (2001)](https://journals.ametsoc.org/view/journals/atsc/58/6/1520-0469_2001_058_0608_afoapi_2.0.co_2.xml)