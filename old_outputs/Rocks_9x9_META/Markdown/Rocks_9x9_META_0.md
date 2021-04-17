
# Parameters

    Name :                      Rocks_9x9_META-0
    Main :                      metateleport
    Level :                     Levels.Rocks
    Hours :                     11.0
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
    Replay size :               100000
    Sample size :               50
    Minutes used :              655 minutes.
    Hours used :                10 hours.

# Profiling


      19103662377 function calls (18991050978 primitive calls) in 39317.73 seconds

##    Ordered by: cumulative time
   List reduced from 470 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 39317.733 39317.733 {built-in method builtins.exec}
                      1    5.187    5.187 39317.733 39317.733 <string>:1(<module>)
                      1   92.942   92.942 39312.546 39312.546 main.py:14(metateleport)
                2448194 6018.502    0.002 10333.572    0.004 replaybuffer.py:27(teleporter_save_data)
                3672291   12.542    0.000 8553.447    0.002 agent.py:27(learn)
                1224097    5.402    0.000 7570.305    0.006 game.py:27(step)
                1224097    7.387    0.000 7306.474    0.006 layers.py:373(step)
                3672291  210.057    0.000 6908.713    0.002 learner.py:42(Qlearn)
                2448194   81.182    0.000 6384.167    0.003 agent.py:51(_learn)
                2448194 4153.534    0.002 5621.310    0.002 agent.py:81(interveen)
                1224097  108.934    0.000 5373.683    0.004 layers.py:18(step)
              122409700  322.455    0.000 5254.742    0.000 layer.py:74(move)
                2448194 3808.782    0.002 4573.906    0.002 replaybuffer.py:23(sample_data)
        126074165/13464465  487.652    0.000 3858.446    0.000 module.py:866(_call_impl)
              122409700  372.955    0.000 3783.244    0.000 layers.py:390(check)
                9792174   26.152    0.000 3594.629    0.000 network.py:24(forward)
              430880362 3563.858    0.000 3563.858    0.000 {built-in method clone}
                9792174  115.969    0.000 3506.211    0.000 container.py:117(forward)
                4895786  114.426    0.000 2943.642    0.001 agent.py:46(__call__)
                3672291   29.567    0.000 2670.038    0.001 optimizer.py:84(wrapper)
                3672291   15.365    0.000 2538.444    0.001 grad_mode.py:24(decorate_context)
                3672291  107.212    0.000 2490.150    0.001 adam.py:55(step)
                3672291  516.138    0.000 2262.858    0.001 _functional.py:53(adam)
                1224097   34.667    0.000 2146.939    0.002 agent.py:145(_learn)
              122409700 1838.304    0.000 1952.826    0.000 layers.py:76(check)
                1224098  138.408    0.000 1915.070    0.002 layers.py:344(update)
                3672291   17.074    0.000 1831.531    0.000 tensor.py:195(backward)
                3672291   15.622    0.000 1813.950    0.000 __init__.py:68(backward)
                3672291 1729.564    0.000 1729.564    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
                1224097  982.453    0.001 1552.981    0.001 agent.py:101(metamodify)
               19584348   44.006    0.000 1301.412    0.000 conv.py:398(forward)
               19584348   27.469    0.000 1237.430    0.000 conv.py:390(_conv_forward)
               19584348 1209.961    0.000 1209.961    0.000 {built-in method conv2d}
              122409700  177.108    0.000  996.986    0.000 layers.py:384(isFree)
               26928328   53.187    0.000  990.298    0.000 linear.py:93(forward)
               26928328   20.717    0.000  910.603    0.000 functional.py:1737(linear)
               11016882  544.285    0.000  901.308    0.000 layer.py:119(update)
                7343980   60.816    0.000  898.622    0.000 agent.py:55(modify_board)
               26928328  885.195    0.000  885.195    0.000 {built-in method torch._C._nn.linear}
              880149543  711.198    0.000  819.878    0.000 layer.py:71(isFree)
              437000245  779.404    0.000  779.404    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               22033144  729.974    0.000  729.974    0.000 {built-in method cat}
                2448194   45.860    0.000  598.657    0.000 replaybuffer.py:19(stacker)
                7343980  579.198    0.000  579.198    0.000 {built-in method torch._C._nn.one_hot}
                6330603  520.464    0.000  520.464    0.000 {built-in method tensor}
               36720502   29.576    0.000  517.360    0.000 activation.py:713(forward)
                1659440   17.300    0.000  509.048    0.000 layers.py:394(restart)
               36720502   29.241    0.000  487.784    0.000 functional.py:1364(leaky_relu)
                1224097   17.922    0.000  477.498    0.000 agent.py:140(__call__)
                3672291    4.455    0.000  455.490    0.000 game.py:23(board)
               36720502  452.836    0.000  452.836    0.000 {built-in method torch._C._nn.leaky_relu}
             1879056435  319.725    0.000  452.084    0.000 enum.py:646(__hash__)
               68549432  434.679    0.000  434.679    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                3672291   70.081    0.000  391.550    0.000 optimizer.py:189(zero_grad)
               68549432  385.536    0.000  385.536    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              122409700  266.850    0.000  328.497    0.000 layers.py:63(check)
                1659440    8.637    0.000  322.264    0.000 level.py:8(__init__)
              122409700  200.247    0.000  321.329    0.000 layers.py:216(check)
              122409800   32.046    0.000  316.510    0.000 {built-in method builtins.all}
              122409700  195.493    0.000  310.663    0.000 layers.py:244(check)
              122409700  192.365    0.000  310.066    0.000 layers.py:230(check)
              367329507   83.490    0.000  298.002    0.000 layers.py:350(<genexpr>)
                4895786  112.964    0.000  295.282    0.000 exploration.py:53(softmaxer)
                1659440   48.561    0.000  284.678    0.000 levels.py:95(generate)
               34274716  274.885    0.000  274.885    0.000 {method 'add' of 'torch._C._TensorBase' objects}
             2863642494  250.362    0.000  250.362    0.000 layer.py:67(positions)
              490094543  232.061    0.000  232.061    0.000 layer.py:114(elements)
                1224097  135.978    0.000  230.586    0.000 collector.py:54(collect)
               34274716  228.341    0.000  228.341    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                4107634   79.142    0.000  209.208    0.000 random.py:315(sample)
               34274716  208.553    0.000  208.553    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               34274716  206.331    0.000  206.331    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              122409800  139.366    0.000  204.250    0.000 layers.py:110(isDone)
              239923096  151.421    0.000  187.157    0.000 tensor.py:906(grad)
               14934960   22.019    0.000  164.859    0.000 layer.py:48(restart)
                3318880   22.128    0.000  163.389    0.000 level.py:41(notUsed)
              122409700  104.051    0.000  157.305    0.000 layers.py:203(check)
               34274716  152.583    0.000  152.583    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                3672291    5.734    0.000  150.907    0.000 loss.py:527(forward)
                3672291   13.104    0.000  145.173    0.000 functional.py:2898(mse_loss)
        1501030300/1501030297  110.357    0.000  137.846    0.000 {built-in method builtins.len}
             1879070806  132.361    0.000  132.361    0.000 {built-in method builtins.hash}
              234194894   88.614    0.000  119.732    0.000 layer.py:98(add)
               11016873  109.252    0.000  109.252    0.000 {built-in method sum}
              108416678   57.078    0.000   94.095    0.000 layer.py:94(remove)
              163927020   63.304    0.000   92.957    0.000 random.py:250(_randbelow_with_getrandbits)
                4895786   91.306    0.000   91.306    0.000 {built-in method multinomial}
                1659540   40.678    0.000   90.522    0.000 layers.py:33(reset)
               91269200   88.985    0.000   88.985    0.000 level.py:32(inverse)
                3672291   88.755    0.000   88.755    0.000 {built-in method torch._C._nn.mse_loss}
               19584348   13.363    0.000   86.529    0.000 flatten.py:39(forward)
                6120485    7.660    0.000   84.543    0.000 tensor.py:525(__rsub__)
              880149543   82.965    0.000   82.965    0.000 layer.py:175(isBlocking)
                3672901   80.180    0.000   80.180    0.000 {built-in method max}
                6120485   75.506    0.000   75.506    0.000 {built-in method rsub}
               19584348   73.166    0.000   73.166    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                2448196   70.463    0.000   70.463    0.000 {built-in method nonzero}
                3672291   14.317    0.000   65.798    0.000 __init__.py:28(_make_grads)
              128523335   65.355    0.000   65.355    0.000 {built-in method torch._C._get_tracing_state}
              102827013   64.859    0.000   64.865    0.000 module.py:934(__getattr__)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-7>
Subject: Job 9452862: <Rocks_9x9_META_0> in cluster <dcc> Done

Job <Rocks_9x9_META_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Tue Mar 23 02:18:34 2021
Job was executed on host(s) <n-62-20-7>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Tue Mar 23 02:18:34 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Tue Mar 23 02:18:34 2021
Terminated at Tue Mar 23 13:14:03 2021
Results reported at Tue Mar 23 13:14:03 2021

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

    CPU time :                                   39296.84 sec.
    Max Memory :                                 3730 MB
    Average Memory :                             3711.75 MB
    Total Requested Memory :                     8192.00 MB
    Delta Memory :                               4462.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   39443 sec.
    Turnaround time :                            39329 sec.

The output (if any) is above this job summary.

