
# Parameters

    Name :                      causal2_9x9_0.3-2
    Main :                      teleport
    Level :                     Levels.Causal2
    Hours :                     10.0
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
    Modified done chance :      0.05
    Miss intervention cost :    -0.2
    Intervention cost :         -0.05
    Replay size :               50000
    Sample size :               50
    Minutes used :              595 minutes.
    Hours used :                9 hours.

# Profiling


      32628368551 function calls (32524507192 primitive calls) in 35711.65 seconds

##    Ordered by: cumulative time
   List reduced from 459 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 35711.654 35711.654 {built-in method builtins.exec}
                      1    0.909    0.909 35711.654 35711.654 <string>:1(<module>)
                      1   72.759   72.759 35710.745 35710.745 main.py:13(teleport)
                3709356   13.357    0.000 9507.523    0.003 agent.py:26(learn)
                1854678    6.491    0.000 9071.112    0.005 game.py:27(step)
                1854678    8.863    0.000 8662.465    0.005 layers.py:373(step)
                3709356  228.155    0.000 8137.125    0.002 learner.py:42(Qlearn)
                1854678 4578.319    0.002 8098.660    0.004 replaybuffer.py:27(teleporter_save_data)
                1854678   52.755    0.000 5676.742    0.003 agent.py:50(_learn)
                1854678  130.637    0.000 4788.958    0.003 layers.py:18(step)
                1854678 3442.539    0.002 4682.565    0.003 agent.py:77(interveen)
              185467800  388.754    0.000 4643.181    0.000 layer.py:74(move)
        116842959/12982611  406.450    0.000 4001.807    0.000 module.py:715(_call_impl)
                1854679  183.238    0.000 3853.518    0.002 layers.py:344(update)
                1854678   46.436    0.000 3810.439    0.002 agent.py:101(_learn)
                9273255   23.276    0.000 3741.114    0.000 network.py:24(forward)
                9273255   99.526    0.000 3665.643    0.000 container.py:115(forward)
                3709356   22.809    0.000 3271.657    0.001 grad_mode.py:23(decorate_context)
                3709356  107.759    0.000 3211.254    0.001 adam.py:55(step)
              185467800  477.211    0.000 2797.203    0.000 layers.py:390(check)
              297807288 2763.945    0.000 2763.945    0.000 {built-in method clone}
                3709356  584.321    0.000 2626.766    0.001 functional.py:53(adam)
                3709221   69.948    0.000 2471.115    0.001 agent.py:45(__call__)
                7472201   58.654    0.000 1920.316    0.000 layers.py:394(restart)
                3709356   20.813    0.000 1887.885    0.001 tensor.py:181(backward)
                3709356   11.456    0.000 1867.072    0.001 __init__.py:68(backward)
                3709356 1777.129    0.000 1777.129    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
                1854678  649.798    0.000 1502.923    0.001 replaybuffer.py:23(sample_data)
                1854678  766.365    0.000 1471.678    0.001 agent.py:59(modify)
                7472201   27.493    0.000 1366.912    0.000 level.py:8(__init__)
               18546510   30.614    0.000 1356.416    0.000 conv.py:422(forward)
               18546510   32.897    0.000 1314.877    0.000 conv.py:414(_conv_forward)
               18546510 1276.135    0.000 1276.135    0.000 {built-in method conv2d}
                7472201   79.106    0.000 1236.334    0.000 levels.py:151(generate)
              185467800  309.745    0.000 1186.991    0.000 layers.py:384(isFree)
               16692111  756.218    0.000 1185.237    0.000 layer.py:119(update)
               24110409   52.202    0.000 1177.341    0.000 linear.py:92(forward)
               24110409   83.942    0.000 1102.957    0.000 functional.py:1669(linear)
               35866797  250.662    0.000 1077.548    0.000 level.py:41(notUsed)
             1632172352  685.038    0.000  877.247    0.000 layer.py:71(isFree)
               16691967  858.485    0.000  858.485    0.000 {built-in method cat}
              233689482  518.875    0.000  856.111    0.000 tensor.py:933(grad)
             3394555358  557.740    0.000  800.570    0.000 enum.py:646(__hash__)
               24110409  776.894    0.000  776.894    0.000 {built-in method addmm}
              303371187  771.269    0.000  771.269    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
                1854678   19.996    0.000  760.813    0.000 agent.py:96(__call__)
                5563899   31.927    0.000  759.539    0.000 agent.py:54(modify_board)
                3709356   73.382    0.000  749.597    0.000 optimizer.py:167(zero_grad)
                1854678   30.530    0.000  730.040    0.000 replaybuffer.py:19(stacker)
                7691663  579.359    0.000  579.359    0.000 {built-in method tensor}
               66768408  528.668    0.000  528.668    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               33383664   25.463    0.000  510.328    0.000 activation.py:713(forward)
              192887444   61.904    0.000  505.785    0.000 {built-in method builtins.all}
                5563899  492.877    0.000  492.877    0.000 {built-in method torch._C._nn.one_hot}
               33383664   39.532    0.000  484.865    0.000 functional.py:1292(leaky_relu)
              185467800  299.379    0.000  479.723    0.000 layers.py:216(check)
              185467800  295.811    0.000  474.844    0.000 layers.py:244(check)
               67249809   47.155    0.000  474.062    0.000 layer.py:48(restart)
                3709356    3.807    0.000  472.832    0.000 game.py:23(board)
              185467800  286.982    0.000  466.043    0.000 layers.py:230(check)
              613561746  151.413    0.000  460.083    0.000 layers.py:350(<genexpr>)
              298603359  149.935    0.000  446.479    0.000 overrides.py:1070(has_torch_function)
               66768408  441.500    0.000  441.500    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               33383664  441.303    0.000  441.303    0.000 {built-in method torch._C._nn.leaky_relu}
              185467800  287.684    0.000  399.496    0.000 layers.py:76(check)
             4418028394  379.282    0.000  379.282    0.000 layer.py:67(positions)
               35866797   22.303    0.000  360.327    0.000 level.py:38(elementsIn)
                7472301  179.627    0.000  359.850    0.000 layers.py:33(reset)
             1722053599  346.760    0.000  346.760    0.000 level.py:32(inverse)
               33384204  310.951    0.000  310.951    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                1854678  179.381    0.000  307.189    0.000 collector.py:54(collect)
              185467900  188.706    0.000  285.943    0.000 layers.py:110(isDone)
               33384204  282.556    0.000  282.556    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              330132481  115.102    0.000  282.132    0.000 {built-in method builtins.any}
              937581088  272.206    0.000  272.206    0.000 layer.py:114(elements)
               33384204  253.911    0.000  253.911    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
                3709221   92.876    0.000  252.487    0.000 exploration.py:53(softmaxer)
             3394569077  242.833    0.000  242.833    0.000 {built-in method builtins.hash}
              185467800  153.080    0.000  235.631    0.000 layers.py:203(check)
              455818498  165.023    0.000  224.905    0.000 layer.py:98(add)
               35866797  108.404    0.000  218.092    0.000 level.py:39(<listcomp>)
               33384204  216.366    0.000  216.366    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              185467800  141.083    0.000  215.995    0.000 layers.py:63(check)
                7419544   32.006    0.000  189.473    0.000 tensor.py:21(wrapped)
               33384204  176.551    0.000  176.551    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                3709356    4.492    0.000  167.524    0.000 loss.py:445(forward)
              628736301  132.711    0.000  164.629    0.000 overrides.py:1083(<genexpr>)
                3709356   18.216    0.000  163.032    0.000 functional.py:2637(mse_loss)
        1612213325/1612213323  105.919    0.000  154.675    0.000 {built-in method builtins.len}
             1632172352  148.383    0.000  148.383    0.000 layer.py:175(isBlocking)
               24110409  139.130    0.000  139.130    0.000 {method 't' of 'torch._C._TensorBase' objects}
              195035247   86.652    0.000  128.392    0.000 layer.py:94(remove)
               11128068  123.832    0.000  123.832    0.000 {built-in method sum}
               35866797   74.409    0.000  119.932    0.000 {built-in method _functools.reduce}
                1854678   44.691    0.000  119.929    0.000 random.py:315(sample)
              650084975  114.315    0.000  114.315    0.000 enum.py:352(<genexpr>)
                5564034   26.165    0.000  108.123    0.000 tensor.py:506(__rsub__)
             1313208330   94.453    0.000   94.453    0.000 {method 'append' of 'list' objects}
               18546510   11.958    0.000   94.280    0.000 flatten.py:39(forward)
                3709356   94.157    0.000   94.157    0.000 {built-in method torch._C._nn.mse_loss}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-6>
Subject: Job 9447955: <causal2_9x9_0.3_2> in cluster <dcc> Done

Job <causal2_9x9_0.3_2> was submitted from host <n-62-30-1> by user <s183905> in cluster <dcc> at Mon Mar 22 13:28:55 2021
Job was executed on host(s) <n-62-20-6>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Mon Mar 22 13:28:57 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Mon Mar 22 13:28:57 2021
Terminated at Mon Mar 22 23:24:15 2021
Results reported at Mon Mar 22 23:24:15 2021

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

    CPU time :                                   35620.43 sec.
    Max Memory :                                 2450 MB
    Average Memory :                             2445.01 MB
    Total Requested Memory :                     8192.00 MB
    Delta Memory :                               5742.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   35779 sec.
    Turnaround time :                            35720 sec.

The output (if any) is above this job summary.

