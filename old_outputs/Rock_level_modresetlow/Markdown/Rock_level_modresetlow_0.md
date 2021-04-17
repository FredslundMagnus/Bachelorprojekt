
# Parameters

    Name :                      Rock_level_modresetlow-0
    Main :                      teleport
    Level :                     Levels.Rocks
    Hours :                     12.0
    Batch :                     100
    Width :                     9
    Height :                    9
    Network1 :                  Networks.Teleporter
    Network2 :                  Networks.Mini
    Learner1 :                  Learners.Qlearn
    Learner2 :                  Learners.Qlearn
    Exploration1 :              Explorations.softmaxer
    Exploration2 :              Explorations.epsilonGreedy
    Layer blocks :              True
    Layer goal :                True
    Layer gold :                False
    Layer keys :                False
    Layer door :                False
    Layer holder :              False
    Layer putter :              False
    Layer rock :                True
    Layer dirt :                True
    Layer diamond1 :            True
    Layer diamond2 :            True
    Layer diamond3 :            True
    Layer diamond4 :            True
    K :                         200000
    Epsilon cap :               0.1
    Softmax cap :               0.02
    Gamma :                     0.98
    Update :                    10000
    Reset chance :              0.002
    Modified done chance :      0.02
    Miss intervention cost :    -0.2
    Intervention cost :         -0.05
    Replay size :               50000
    Sample size :               50
    Minutes used :              715 minutes.
    Hours used :                11 hours.

# Profiling


      47794579202 function calls (47638508219 primitive calls) in 42914.48 seconds

##    Ordered by: cumulative time
   List reduced from 470 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 42914.482 42914.482 {built-in method builtins.exec}
                      1    0.912    0.912 42914.482 42914.482 <string>:1(<module>)
                      1  112.277  112.277 42913.569 42913.569 main.py:13(teleport)
                2788155    9.753    0.000 18458.819    0.007 game.py:27(step)
                2788155   12.994    0.000 17874.179    0.006 layers.py:373(step)
                5576310   19.588    0.000 11639.424    0.002 agent.py:26(learn)
                2788155  213.027    0.000 11612.560    0.004 layers.py:18(step)
              278815500  581.449    0.000 11376.268    0.000 layer.py:74(move)
                5576310  309.351    0.000 9794.784    0.002 learner.py:42(Qlearn)
              278815500  837.579    0.000 8439.429    0.000 layers.py:390(check)
                2788155   88.538    0.000 6953.897    0.002 agent.py:50(_learn)
                2788156  277.417    0.000 6231.830    0.002 layers.py:344(update)
        175581498/19511526  645.187    0.000 5222.868    0.000 module.py:866(_call_impl)
               13935216   37.329    0.000 4846.392    0.000 network.py:24(forward)
               13935216  158.701    0.000 4729.234    0.000 container.py:117(forward)
                2788155   78.562    0.000 4656.093    0.002 agent.py:101(_learn)
              278815500 3775.588    0.000 4512.820    0.000 layers.py:76(check)
                2788155 2404.775    0.001 4106.522    0.001 replaybuffer.py:27(teleporter_save_data)
                5576310   43.681    0.000 3794.843    0.001 optimizer.py:84(wrapper)
                5576310   22.698    0.000 3600.010    0.001 grad_mode.py:24(decorate_context)
                5576310  140.014    0.000 3529.482    0.001 adam.py:55(step)
                2788155 1716.891    0.001 3316.025    0.001 agent.py:77(interveen)
                5570751  116.587    0.000 3233.284    0.001 agent.py:45(__call__)
                5576310  737.114    0.000 3220.843    0.001 _functional.py:53(adam)
                9951589   82.757    0.000 2684.364    0.000 layers.py:394(restart)
                5576310   20.582    0.000 2505.505    0.000 tensor.py:195(backward)
                5576310   20.511    0.000 2484.206    0.000 __init__.py:68(backward)
               25093404 1681.222    0.000 2465.442    0.000 layer.py:119(update)
                5576310 2365.047    0.000 2365.047    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
              278815500  488.570    0.000 2036.766    0.000 layers.py:384(isFree)
                2788155  970.662    0.000 1826.117    0.001 replaybuffer.py:23(sample_data)
               27870432   57.825    0.000 1776.350    0.000 conv.py:398(forward)
                2788155 1067.344    0.000 1729.426    0.001 agent.py:59(modify)
               27870432   35.568    0.000 1694.342    0.000 conv.py:390(_conv_forward)
                9951589   38.543    0.000 1683.931    0.000 level.py:8(__init__)
               27870432 1658.774    0.000 1658.774    0.000 {built-in method conv2d}
             2354320662 1258.973    0.000 1548.196    0.000 layer.py:71(isFree)
                9951589  238.998    0.000 1503.752    0.000 levels.py:95(generate)
              170399808 1417.587    0.000 1417.587    0.000 {built-in method clone}
               36229338   71.415    0.000 1313.546    0.000 linear.py:93(forward)
               36229338   27.933    0.000 1210.597    0.000 functional.py:1737(linear)
               36229338 1175.982    0.000 1175.982    0.000 {built-in method torch._C._nn.linear}
             4895607938  794.281    0.000 1148.141    0.000 enum.py:646(__hash__)
                2788155   34.629    0.000 1004.988    0.000 agent.py:96(__call__)
                8358906   45.007    0.000  996.558    0.000 agent.py:54(modify_board)
               89564301  123.023    0.000  891.386    0.000 layer.py:48(restart)
               19903178  115.590    0.000  848.851    0.000 level.py:41(notUsed)
               11521558  836.688    0.000  836.688    0.000 {built-in method tensor}
               25087836  826.817    0.000  826.817    0.000 {built-in method cat}
              278815500  441.257    0.000  714.782    0.000 layers.py:230(check)
              278815600   80.301    0.000  699.719    0.000 {built-in method builtins.all}
                5576310    5.895    0.000  696.892    0.000 game.py:23(board)
              278815500  428.480    0.000  695.539    0.000 layers.py:216(check)
               50164554   35.797    0.000  693.646    0.000 activation.py:713(forward)
              278815500  416.601    0.000  684.300    0.000 layers.py:244(check)
                2788155   46.799    0.000  673.849    0.000 replaybuffer.py:19(stacker)
                8358906  661.175    0.000  661.175    0.000 {built-in method torch._C._nn.one_hot}
               50164554   37.411    0.000  657.849    0.000 functional.py:1364(leaky_relu)
              891443504  200.625    0.000  649.977    0.000 layers.py:350(<genexpr>)
             1314806038  469.712    0.000  627.954    0.000 layer.py:98(add)
              100373580  614.384    0.000  614.384    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               50164554  612.895    0.000  612.895    0.000 {built-in method torch._C._nn.leaky_relu}
              278815500  376.910    0.000  585.591    0.000 layers.py:63(check)
                5576310  102.715    0.000  571.441    0.000 optimizer.py:189(zero_grad)
             6531174638  569.801    0.000  569.801    0.000 layer.py:67(positions)
              100373580  562.039    0.000  562.039    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              617709233  282.283    0.000  548.130    0.000 layer.py:94(remove)
             2665461470  540.072    0.000  540.072    0.000 layer.py:114(elements)
                9951689  239.432    0.000  483.163    0.000 layers.py:33(reset)
              547337395  446.579    0.000  446.579    0.000 level.py:32(inverse)
               12739744  159.445    0.000  446.373    0.000 random.py:315(sample)
              278815600  279.054    0.000  420.808    0.000 layers.py:110(isDone)
                2788155  220.828    0.000  376.849    0.000 collector.py:54(collect)
               50186790  374.374    0.000  374.374    0.000 {method 'add' of 'torch._C._TensorBase' objects}
             4895628353  353.864    0.000  353.864    0.000 {built-in method builtins.hash}
              178758714  344.152    0.000  344.152    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              278815500  219.855    0.000  340.992    0.000 layers.py:203(check)
                5570751  125.039    0.000  326.844    0.000 exploration.py:53(softmaxer)
               50186790  320.782    0.000  320.782    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               50186790  302.103    0.000  302.103    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               50186790  298.275    0.000  298.275    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              351307584  214.701    0.000  266.797    0.000 tensor.py:906(grad)
              278815500  112.839    0.000  266.773    0.000 layers.py:99(<listcomp>)
             3991517901  259.006    0.000  259.006    0.000 {method 'append' of 'list' objects}
        2829643291/2829643289  187.785    0.000  223.814    0.000 {built-in method builtins.len}
             2354320662  223.698    0.000  223.698    0.000 layer.py:175(isBlocking)
               50186790  222.616    0.000  222.616    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                5576310    6.885    0.000  221.822    0.000 loss.py:527(forward)
               19903178   15.614    0.000  218.606    0.000 level.py:38(elementsIn)
              388266500  150.806    0.000  218.489    0.000 random.py:250(_randbelow_with_getrandbits)
              617709233  218.083    0.000  218.083    0.000 {method 'remove' of 'list' objects}
                5576310   20.196    0.000  214.936    0.000 functional.py:2898(mse_loss)
               16728930  164.061    0.000  164.061    0.000 {built-in method sum}
                5576310  130.692    0.000  130.692    0.000 {built-in method torch._C._nn.mse_loss}
               19903178   63.370    0.000  123.966    0.000 level.py:39(<listcomp>)
               27870432   21.314    0.000  123.748    0.000 flatten.py:39(forward)
                5577145  118.534    0.000  118.534    0.000 {built-in method max}
                9951589   54.206    0.000  115.697    0.000 level.py:16(<dictcomp>)
                8364465   10.180    0.000  112.251    0.000 tensor.py:525(__rsub__)
               27870432  102.434    0.000  102.434    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-6>
Subject: Job 9441989: <Rock_level_modresetlow_0> in cluster <dcc> Done

Job <Rock_level_modresetlow_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Sat Mar 20 01:13:12 2021
Job was executed on host(s) <n-62-20-6>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sat Mar 20 13:08:40 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sat Mar 20 13:08:40 2021
Terminated at Sun Mar 21 01:04:03 2021
Results reported at Sun Mar 21 01:04:03 2021

Your job looked like:

------------------------------------------------------------
# LSBATCH: User input
#!/bin/sh
#BSUB -q hpc
#BSUB -q gpuv100
#BSUB -gpu "num=1:mode=exclusive_process"
#BSUB -n 1
#BSUB -R "rusage[mem=8G]"
#BSUB -R "span[hosts=1]"
#BSUB -W 1440
# end of BSUB options
cd ..
module -s load python3
source ../project-env/bin/activate

python main.py $LSB_PROJECT_NAME


------------------------------------------------------------

Successfully completed.

Resource usage summary:

    CPU time :                                   42804.43 sec.
    Max Memory :                                 6199 MB
    Average Memory :                             4429.80 MB
    Total Requested Memory :                     8192.00 MB
    Delta Memory :                               1993.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   43003 sec.
    Turnaround time :                            85851 sec.

The output (if any) is above this job summary.

