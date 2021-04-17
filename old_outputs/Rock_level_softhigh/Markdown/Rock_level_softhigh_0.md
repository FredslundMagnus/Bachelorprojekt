
# Parameters

    Name :                      Rock_level_softhigh-0
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
    Softmax cap :               0.05
    Gamma :                     0.98
    Update :                    10000
    Reset chance :              0.002
    Modified done chance :      0.05
    Miss intervention cost :    -0.2
    Intervention cost :         -0.05
    Replay size :               50000
    Sample size :               50
    Minutes used :              715 minutes.
    Hours used :                11 hours.

# Profiling


      38518066839 function calls (38382934964 primitive calls) in 42914.20 seconds

##    Ordered by: cumulative time
   List reduced from 470 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 42914.198 42914.198 {built-in method builtins.exec}
                      1    0.986    0.986 42914.198 42914.198 <string>:1(<module>)
                      1  102.420  102.420 42913.212 42913.212 main.py:13(teleport)
                2413091    9.739    0.000 16471.564    0.007 game.py:27(step)
                2413091   11.231    0.000 15942.113    0.007 layers.py:373(step)
                4826182   16.493    0.000 11075.991    0.002 agent.py:26(learn)
                2413091  209.910    0.000 10858.491    0.004 layers.py:18(step)
              241309100  576.129    0.000 10625.969    0.000 layer.py:74(move)
                4826182  297.258    0.000 9337.474    0.002 learner.py:42(Qlearn)
              241309100  790.193    0.000 7908.143    0.000 layers.py:390(check)
                2413091   81.540    0.000 6624.334    0.003 agent.py:50(_learn)
                2413091 3653.478    0.002 6242.724    0.003 replaybuffer.py:27(teleporter_save_data)
                2413092  268.428    0.000 5056.574    0.002 layers.py:344(update)
        152022315/16891451  603.802    0.000 4949.088    0.000 module.py:866(_call_impl)
               12065269   36.214    0.000 4594.648    0.000 network.py:24(forward)
               12065269  147.054    0.000 4479.532    0.000 container.py:117(forward)
                2413091   71.513    0.000 4425.684    0.002 agent.py:101(_learn)
              241309100 3643.092    0.000 4200.513    0.000 layers.py:76(check)
                2413091 2571.610    0.001 4085.492    0.002 agent.py:77(interveen)
                4826182   43.064    0.000 3632.603    0.001 optimizer.py:84(wrapper)
                4826182   20.402    0.000 3445.046    0.001 grad_mode.py:24(decorate_context)
                4826182  133.754    0.000 3378.875    0.001 adam.py:55(step)
                4826182  708.713    0.000 3080.769    0.001 _functional.py:53(adam)
                4825996  111.018    0.000 3059.945    0.001 agent.py:45(__call__)
                4826182   18.524    0.000 2384.483    0.000 tensor.py:195(backward)
                4826182   18.698    0.000 2365.293    0.000 __init__.py:68(backward)
                4826182 2253.098    0.000 2253.098    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
              237662458 2118.909    0.000 2118.909    0.000 {built-in method clone}
               21717828 1371.485    0.000 2067.682    0.000 layer.py:119(update)
                6502624   60.560    0.000 1943.404    0.000 layers.py:394(restart)
              241309100  424.342    0.000 1836.105    0.000 layers.py:384(isFree)
                2413091  900.218    0.000 1696.713    0.001 replaybuffer.py:23(sample_data)
               24130538   55.701    0.000 1677.352    0.000 conv.py:398(forward)
                2413091  990.554    0.000 1616.715    0.001 agent.py:59(modify)
               24130538   32.393    0.000 1598.272    0.000 conv.py:390(_conv_forward)
               24130538 1565.879    0.000 1565.879    0.000 {built-in method conv2d}
             1990909482 1150.986    0.000 1411.763    0.000 layer.py:71(isFree)
               31369625   71.098    0.000 1244.224    0.000 linear.py:93(forward)
                6502624   28.462    0.000 1223.265    0.000 level.py:8(__init__)
               31369625   27.028    0.000 1143.159    0.000 functional.py:1737(linear)
               31369625 1109.444    0.000 1109.444    0.000 {built-in method torch._C._nn.linear}
                6502624  172.574    0.000 1093.042    0.000 levels.py:95(generate)
             4015944704  745.574    0.000 1060.746    0.000 enum.py:646(__hash__)
                2413091   31.222    0.000  952.591    0.000 agent.py:96(__call__)
                7239087   43.154    0.000  937.370    0.000 agent.py:54(modify_board)
               21717633  768.992    0.000  768.992    0.000 {built-in method cat}
                9982625  747.783    0.000  747.783    0.000 {built-in method tensor}
              241309100  420.852    0.000  683.534    0.000 layers.py:216(check)
              241309200   74.023    0.000  675.242    0.000 {built-in method builtins.all}
               43434894   34.932    0.000  666.520    0.000 activation.py:713(forward)
              241309100  408.987    0.000  657.205    0.000 layers.py:244(check)
              241309100  394.781    0.000  648.671    0.000 layers.py:230(check)
               58523616   89.224    0.000  640.255    0.000 layer.py:48(restart)
               43434894   35.798    0.000  631.588    0.000 functional.py:1364(leaky_relu)
              751892649  189.510    0.000  630.953    0.000 layers.py:350(<genexpr>)
                2413091   43.581    0.000  622.849    0.000 replaybuffer.py:19(stacker)
                7239087  617.128    0.000  617.128    0.000 {built-in method torch._C._nn.one_hot}
               13005248   86.765    0.000  616.081    0.000 level.py:41(notUsed)
                4826182    4.841    0.000  613.508    0.000 game.py:23(board)
               86871276  595.625    0.000  595.625    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               43434894  588.440    0.000  588.440    0.000 {built-in method torch._C._nn.leaky_relu}
                4826182   96.401    0.000  549.533    0.000 optimizer.py:189(zero_grad)
               86871276  538.517    0.000  538.517    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
             5659080537  537.295    0.000  537.295    0.000 layer.py:67(positions)
              241309100  351.342    0.000  532.570    0.000 layers.py:63(check)
              244901545  516.533    0.000  516.533    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              886246689  351.015    0.000  474.142    0.000 layer.py:98(add)
             1809733684  459.336    0.000  459.336    0.000 layer.py:114(elements)
              241309200  274.230    0.000  416.463    0.000 layers.py:110(isDone)
              428369570  218.127    0.000  416.426    0.000 layer.py:94(remove)
                2413091  214.153    0.000  365.527    0.000 collector.py:54(collect)
                8915715  131.314    0.000  364.808    0.000 random.py:315(sample)
               43435638  353.462    0.000  353.462    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                6502724  172.614    0.000  347.285    0.000 layers.py:33(reset)
              241309100  212.875    0.000  330.066    0.000 layers.py:203(check)
              357644320  321.651    0.000  321.651    0.000 level.py:32(inverse)
             4015962455  315.175    0.000  315.175    0.000 {built-in method builtins.hash}
                4825996  116.492    0.000  309.295    0.000 exploration.py:53(softmaxer)
               43435638  308.988    0.000  308.988    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               43435638  283.208    0.000  283.208    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               43435638  281.115    0.000  281.115    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              304049520  208.367    0.000  259.771    0.000 tensor.py:906(grad)
        2474954631/2474954629  181.200    0.000  216.803    0.000 {built-in method builtins.len}
               43435638  213.367    0.000  213.367    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                4826182    8.305    0.000  208.766    0.000 loss.py:527(forward)
             2741546564  205.716    0.000  205.716    0.000 {method 'append' of 'list' objects}
                4826182   18.764    0.000  200.461    0.000 functional.py:2898(mse_loss)
             1990909482  198.798    0.000  198.798    0.000 layer.py:175(isBlocking)
              241309100   87.585    0.000  195.465    0.000 layers.py:99(<listcomp>)
              283279926  121.121    0.000  175.407    0.000 random.py:250(_randbelow_with_getrandbits)
              428369570  159.131    0.000  159.131    0.000 {method 'remove' of 'list' objects}
               13005248   11.947    0.000  158.748    0.000 level.py:38(elementsIn)
               14478546  157.576    0.000  157.576    0.000 {built-in method sum}
                4826182  123.201    0.000  123.201    0.000 {built-in method torch._C._nn.mse_loss}
               24130538   16.940    0.000  117.113    0.000 flatten.py:39(forward)
                4826905  112.705    0.000  112.705    0.000 {built-in method max}
                7239273    9.958    0.000  106.484    0.000 tensor.py:525(__rsub__)
               24130538  100.173    0.000  100.173    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                4825996   96.897    0.000   96.897    0.000 {built-in method multinomial}
                7239273   94.685    0.000   94.685    0.000 {built-in method rsub}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-13>
Subject: Job 9441985: <Rock_level_softhigh_0> in cluster <dcc> Done

Job <Rock_level_softhigh_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Sat Mar 20 01:13:11 2021
Job was executed on host(s) <n-62-20-13>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sat Mar 20 01:13:12 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sat Mar 20 01:13:12 2021
Terminated at Sat Mar 20 13:08:38 2021
Results reported at Sat Mar 20 13:08:38 2021

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

    CPU time :                                   42803.05 sec.
    Max Memory :                                 5730 MB
    Average Memory :                             4194.93 MB
    Total Requested Memory :                     8192.00 MB
    Delta Memory :                               2462.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   42925 sec.
    Turnaround time :                            42927 sec.

The output (if any) is above this job summary.

