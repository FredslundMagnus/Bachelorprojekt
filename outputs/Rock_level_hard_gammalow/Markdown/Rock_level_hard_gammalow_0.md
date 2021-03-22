
# Parameters

    Name :                      Rock_level_hard_gammalow-0
    Main :                      teleport
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
    Gamma :                     0.95
    Update :                    10000
    Reset chance :              0.002
    Modified done chance :      0.05
    Miss intervention cost :    -0.2
    Intervention cost :         -0.05
    Replay size :               50000
    Sample size :               50
    Minutes used :              655 minutes.
    Hours used :                10 hours.

# Profiling


      32616398500 function calls (32503354641 primitive calls) in 39312.26 seconds

##    Ordered by: cumulative time
   List reduced from 470 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 39312.263 39312.263 {built-in method builtins.exec}
                      1    0.923    0.923 39312.263 39312.263 <string>:1(<module>)
                      1   82.926   82.926 39311.339 39311.339 main.py:13(teleport)
                2018645    7.901    0.000 13381.355    0.007 game.py:27(step)
                2018645    9.776    0.000 12916.110    0.006 layers.py:373(step)
                4037290   13.926    0.000 11117.544    0.003 agent.py:26(learn)
                4037290  286.925    0.000 9581.596    0.002 learner.py:42(Qlearn)
                2018645  158.152    0.000 8849.972    0.004 layers.py:18(step)
              201864500  403.474    0.000 8673.941    0.000 layer.py:74(move)
              201864500  651.619    0.000 6728.648    0.000 layers.py:390(check)
                2018645   57.874    0.000 6603.427    0.003 agent.py:50(_learn)
                2018645 3463.195    0.002 6275.353    0.003 replaybuffer.py:27(teleporter_save_data)
                2018645   50.015    0.000 4491.230    0.002 agent.py:101(_learn)
        127173257/14130409  499.722    0.000 4474.702    0.000 module.py:866(_call_impl)
               10093119   29.219    0.000 4163.776    0.000 network.py:24(forward)
               10093119  129.227    0.000 4074.038    0.000 container.py:117(forward)
                4037290   33.825    0.000 4063.569    0.001 optimizer.py:84(wrapper)
                2018646  202.757    0.000 4044.174    0.002 layers.py:344(update)
                2018645 2629.496    0.001 4009.052    0.002 agent.py:77(interveen)
                4037290   17.141    0.000 3901.134    0.001 grad_mode.py:24(decorate_context)
              201864500 3386.765    0.000 3873.810    0.000 layers.py:76(check)
                4037290  110.470    0.000 3846.100    0.001 adam.py:55(step)
                4037290  786.414    0.000 3608.910    0.001 _functional.py:53(adam)
                4037184   82.143    0.000 2773.332    0.001 agent.py:45(__call__)
                4037290   18.612    0.000 2404.146    0.001 tensor.py:195(backward)
                4037290   15.811    0.000 2384.929    0.001 __init__.py:68(backward)
                4037290 2281.385    0.001 2281.385    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
              196124998 2275.281    0.000 2275.281    0.000 {built-in method clone}
                6024114   51.823    0.000 1646.207    0.000 layers.py:394(restart)
               18167814 1075.822    0.000 1617.712    0.000 layer.py:119(update)
                2018645  977.098    0.000 1569.090    0.001 agent.py:59(modify)
               20186238   44.100    0.000 1485.962    0.000 conv.py:398(forward)
               20186238   26.247    0.000 1423.405    0.000 conv.py:390(_conv_forward)
               20186238 1397.158    0.000 1397.158    0.000 {built-in method conv2d}
              201864500  314.471    0.000 1357.262    0.000 layers.py:384(isFree)
                2018645  693.649    0.000 1355.481    0.001 replaybuffer.py:23(sample_data)
               26242067   54.674    0.000 1158.528    0.000 linear.py:93(forward)
               26242067   22.584    0.000 1080.612    0.000 functional.py:1737(linear)
               26242067 1053.016    0.000 1053.016    0.000 {built-in method torch._C._nn.linear}
                6024114   23.323    0.000 1045.783    0.000 level.py:8(__init__)
             1529515587  857.709    0.000 1042.791    0.000 layer.py:71(isFree)
                6024114  147.834    0.000  939.495    0.000 levels.py:95(generate)
                6055829   39.116    0.000  861.009    0.000 agent.py:54(modify_board)
                2018645   24.071    0.000  857.889    0.000 agent.py:96(__call__)
             3410916654  555.920    0.000  783.350    0.000 enum.py:646(__hash__)
               72671220  733.677    0.000  733.677    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               18167699  676.099    0.000  676.099    0.000 {built-in method cat}
                8364463  654.224    0.000  654.224    0.000 {built-in method tensor}
               36335186   27.081    0.000  651.947    0.000 activation.py:713(forward)
               72671220  646.284    0.000  646.284    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               36335186   29.746    0.000  624.866    0.000 functional.py:1364(leaky_relu)
              202180827  595.757    0.000  595.757    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               36335186  589.012    0.000  589.012    0.000 {built-in method torch._C._nn.leaky_relu}
                4037290   92.071    0.000  569.081    0.000 optimizer.py:189(zero_grad)
                6055829  553.672    0.000  553.672    0.000 {built-in method torch._C._nn.one_hot}
               54217026   74.310    0.000  532.598    0.000 layer.py:48(restart)
                2018645   36.064    0.000  531.452    0.000 replaybuffer.py:19(stacker)
                4037290    4.303    0.000  525.504    0.000 game.py:23(board)
               12048228   68.150    0.000  514.359    0.000 level.py:41(notUsed)
              201864500  320.109    0.000  513.901    0.000 layers.py:216(check)
              201864600   55.198    0.000  500.313    0.000 {built-in method builtins.all}
              201864500  311.587    0.000  498.853    0.000 layers.py:244(check)
              201864500  303.161    0.000  494.794    0.000 layers.py:230(check)
              622807143  140.539    0.000  467.701    0.000 layers.py:350(<genexpr>)
             4688301739  424.169    0.000  424.169    0.000 layer.py:67(positions)
               36335610  411.493    0.000  411.493    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                2018645  243.251    0.000  402.449    0.000 collector.py:54(collect)
              201864500  252.121    0.000  382.333    0.000 layers.py:63(check)
              792212110  273.223    0.000  370.351    0.000 layer.py:98(add)
             1617063325  363.186    0.000  363.186    0.000 layer.py:114(elements)
               36335610  347.063    0.000  347.063    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               36335610  337.938    0.000  337.938    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               36335610  335.421    0.000  335.421    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              356390116  156.088    0.000  324.773    0.000 layer.py:94(remove)
                8042759  113.305    0.000  315.174    0.000 random.py:315(sample)
              201864600  203.667    0.000  308.618    0.000 layers.py:110(isDone)
                4037184  106.260    0.000  293.371    0.000 exploration.py:53(softmaxer)
                6024214  143.381    0.000  288.246    0.000 layers.py:33(reset)
              301205700  274.307    0.000  274.307    0.000 level.py:32(inverse)
              201864500  174.438    0.000  263.381    0.000 layers.py:203(check)
               36335610  256.981    0.000  256.981    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
             3410931525  227.433    0.000  227.433    0.000 {built-in method builtins.hash}
              254349324  171.987    0.000  211.546    0.000 tensor.py:906(grad)
                4037290    5.979    0.000  193.080    0.000 loss.py:527(forward)
                4037290   14.882    0.000  187.101    0.000 functional.py:2898(mse_loss)
        2111119359/2111119357  147.192    0.000  177.172    0.000 {built-in method builtins.len}
               12111870  168.690    0.000  168.690    0.000 {built-in method sum}
              201864500   75.274    0.000  167.514    0.000 layers.py:99(<listcomp>)
             2421753563  161.271    0.000  161.271    0.000 {method 'append' of 'list' objects}
              281705693  108.140    0.000  155.587    0.000 random.py:250(_randbelow_with_getrandbits)
              356390116  140.243    0.000  140.243    0.000 {method 'remove' of 'list' objects}
             1529515587  139.777    0.000  139.777    0.000 layer.py:175(isBlocking)
               12048228    9.773    0.000  131.888    0.000 level.py:38(elementsIn)
                4037290  122.868    0.000  122.868    0.000 {built-in method torch._C._nn.mse_loss}
               20186238   13.681    0.000  113.853    0.000 flatten.py:39(forward)
                6055935    9.521    0.000  107.941    0.000 tensor.py:525(__rsub__)
                4037894  104.848    0.000  104.848    0.000 {built-in method max}
               20186238  100.172    0.000  100.172    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                6055935   96.929    0.000   96.929    0.000 {built-in method rsub}
                4037184   93.332    0.000   93.332    0.000 {built-in method multinomial}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-7>
Subject: Job 9444628: <Rock_level_hard_gammalow_0> in cluster <dcc> Done

Job <Rock_level_hard_gammalow_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Sun Mar 21 02:08:58 2021
Job was executed on host(s) <n-62-20-7>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sun Mar 21 13:04:27 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sun Mar 21 13:04:27 2021
Terminated at Mon Mar 22 00:00:42 2021
Results reported at Mon Mar 22 00:00:42 2021

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

    CPU time :                                   39285.79 sec.
    Max Memory :                                 2680 MB
    Average Memory :                             2664.42 MB
    Total Requested Memory :                     8192.00 MB
    Delta Memory :                               5512.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   39395 sec.
    Turnaround time :                            78704 sec.

The output (if any) is above this job summary.

