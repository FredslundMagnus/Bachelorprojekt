
# Parameters

    Name :                      Rock_level_interventionlow-0
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
    Modified done chance :      0.05
    Miss intervention cost :    -0.2
    Intervention cost :         -0.1
    Replay size :               50000
    Sample size :               50
    Minutes used :              715 minutes.
    Hours used :                11 hours.

# Profiling


      46396058394 function calls (46244853531 primitive calls) in 42912.74 seconds

##    Ordered by: cumulative time
   List reduced from 470 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 42912.741 42912.741 {built-in method builtins.exec}
                      1    0.900    0.900 42912.741 42912.741 <string>:1(<module>)
                      1  112.273  112.273 42911.841 42911.841 main.py:13(teleport)
                2700129    9.235    0.000 18351.781    0.007 game.py:27(step)
                2700129   13.069    0.000 17777.783    0.007 layers.py:373(step)
                2700129  216.133    0.000 11505.026    0.004 layers.py:18(step)
                5400258   18.694    0.000 11435.687    0.002 agent.py:26(learn)
              270012900  567.873    0.000 11266.579    0.000 layer.py:74(move)
                5400258  307.079    0.000 9631.374    0.002 learner.py:42(Qlearn)
              270012900  799.724    0.000 8412.810    0.000 layers.py:390(check)
                2700129   86.176    0.000 6817.381    0.003 agent.py:50(_learn)
                2700130  276.370    0.000 6241.977    0.002 layers.py:344(update)
        170104474/18900622  622.981    0.000 5105.248    0.000 module.py:866(_call_impl)
               13500364   36.246    0.000 4741.137    0.000 network.py:24(forward)
               13500364  150.805    0.000 4625.875    0.000 container.py:117(forward)
                2700129   74.852    0.000 4589.983    0.002 agent.py:101(_learn)
              270012900 3838.335    0.000 4536.430    0.000 layers.py:76(check)
                2700129 2585.987    0.001 4407.306    0.002 replaybuffer.py:27(teleporter_save_data)
                5400258   43.451    0.000 3740.832    0.001 optimizer.py:84(wrapper)
                5400258   22.388    0.000 3548.591    0.001 grad_mode.py:24(decorate_context)
                5400258  137.653    0.000 3477.650    0.001 adam.py:55(step)
                2700129 1816.768    0.001 3382.466    0.001 agent.py:77(interveen)
                5400258  721.764    0.000 3171.462    0.001 _functional.py:53(adam)
                5399977  116.240    0.000 3166.700    0.001 agent.py:45(__call__)
                9946961   84.680    0.000 2704.560    0.000 layers.py:394(restart)
                5400258   19.947    0.000 2469.079    0.000 tensor.py:195(backward)
               24301170 1664.233    0.000 2453.189    0.000 layer.py:119(update)
                5400258   20.709    0.000 2448.341    0.000 __init__.py:68(backward)
                5400258 2329.378    0.000 2329.378    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
              270012900  434.156    0.000 2001.258    0.000 layers.py:384(isFree)
                2700129  975.397    0.000 1813.626    0.001 replaybuffer.py:23(sample_data)
               27000728   58.246    0.000 1740.360    0.000 conv.py:398(forward)
                2700129 1055.854    0.000 1720.255    0.001 agent.py:59(modify)
                9946961   39.460    0.000 1696.574    0.000 level.py:8(__init__)
               27000728   35.576    0.000 1657.744    0.000 conv.py:390(_conv_forward)
               27000728 1622.168    0.000 1622.168    0.000 {built-in method conv2d}
             2249295936 1291.881    0.000 1567.102    0.000 layer.py:71(isFree)
                9946961  242.536    0.000 1517.339    0.000 levels.py:95(generate)
              183070668 1515.122    0.000 1515.122    0.000 {built-in method clone}
               35100834   67.718    0.000 1293.401    0.000 linear.py:93(forward)
               35100834   26.925    0.000 1193.459    0.000 functional.py:1737(linear)
               35100834 1160.403    0.000 1160.403    0.000 {built-in method torch._C._nn.linear}
             4780811316  800.604    0.000 1131.248    0.000 enum.py:646(__hash__)
                8100106   45.749    0.000  987.254    0.000 agent.py:54(modify_board)
                2700129   32.996    0.000  982.199    0.000 agent.py:96(__call__)
               89522649  128.504    0.000  896.269    0.000 layer.py:48(restart)
               19893922  117.904    0.000  852.278    0.000 level.py:41(notUsed)
               11161544  821.773    0.000  821.773    0.000 {built-in method tensor}
               24300880  806.754    0.000  806.754    0.000 {built-in method cat}
              270013000   78.858    0.000  702.860    0.000 {built-in method builtins.all}
              270012900  434.585    0.000  696.685    0.000 layers.py:216(check)
              270012900  422.496    0.000  690.830    0.000 layers.py:230(check)
               48601198   35.761    0.000  686.508    0.000 activation.py:713(forward)
                5400258    5.148    0.000  684.203    0.000 game.py:23(board)
              270012900  416.790    0.000  672.547    0.000 layers.py:244(check)
                2700129   46.583    0.000  658.038    0.000 replaybuffer.py:19(stacker)
                8100106  656.106    0.000  656.106    0.000 {built-in method torch._C._nn.one_hot}
              861749869  203.266    0.000  654.098    0.000 layers.py:350(<genexpr>)
               48601198   38.438    0.000  650.747    0.000 functional.py:1364(leaky_relu)
               97204644  612.007    0.000  612.007    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              270012900  400.738    0.000  608.467    0.000 layers.py:63(check)
               48601198  605.018    0.000  605.018    0.000 {built-in method torch._C._nn.leaky_relu}
             1274982495  438.689    0.000  592.944    0.000 layer.py:98(add)
                5400258  100.488    0.000  563.083    0.000 optimizer.py:189(zero_grad)
             6323631246  551.704    0.000  551.704    0.000 layer.py:67(positions)
               97204644  548.910    0.000  548.910    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
             2585139376  546.241    0.000  546.241    0.000 layer.py:114(elements)
              572927806  247.546    0.000  507.228    0.000 layer.py:94(remove)
                9947061  243.986    0.000  487.124    0.000 layers.py:33(reset)
               12647090  162.292    0.000  449.878    0.000 random.py:315(sample)
              547082855  447.103    0.000  447.103    0.000 level.py:32(inverse)
              270013000  280.267    0.000  421.990    0.000 layers.py:110(isDone)
                2700129  218.928    0.000  372.721    0.000 collector.py:54(collect)
               48602322  367.533    0.000  367.533    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              191170774  362.850    0.000  362.850    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              270012900  221.804    0.000  340.559    0.000 layers.py:203(check)
             4780831155  330.647    0.000  330.647    0.000 {built-in method builtins.hash}
                5399977  119.271    0.000  318.377    0.000 exploration.py:53(softmaxer)
               48602322  317.691    0.000  317.691    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               48602322  296.752    0.000  296.752    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               48602322  295.438    0.000  295.438    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              340216308  213.421    0.000  264.885    0.000 tensor.py:906(grad)
              270012900  116.825    0.000  255.823    0.000 layers.py:99(<listcomp>)
             3858762490  251.718    0.000  251.718    0.000 {method 'append' of 'list' objects}
               48602322  220.969    0.000  220.969    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
               19893922   16.221    0.000  219.233    0.000 level.py:38(elementsIn)
              383747381  151.208    0.000  218.313    0.000 random.py:250(_randbelow_with_getrandbits)
        2756358555/2756358553  181.491    0.000  217.947    0.000 {built-in method builtins.len}
                5400258    8.247    0.000  215.929    0.000 loss.py:527(forward)
              572927806  215.033    0.000  215.033    0.000 {method 'remove' of 'list' objects}
             2249295936  212.731    0.000  212.731    0.000 layer.py:175(isBlocking)
                5400258   19.990    0.000  207.682    0.000 functional.py:2898(mse_loss)
               16200774  160.855    0.000  160.855    0.000 {built-in method sum}
                5400258  126.913    0.000  126.913    0.000 {built-in method torch._C._nn.mse_loss}
               19893922   63.083    0.000  122.971    0.000 level.py:39(<listcomp>)
                5401067  116.556    0.000  116.556    0.000 {built-in method max}
               27000728   16.593    0.000  115.157    0.000 flatten.py:39(forward)
                9946961   53.957    0.000  113.719    0.000 level.py:16(<dictcomp>)
                8100387   11.086    0.000  111.111    0.000 tensor.py:525(__rsub__)
                5399977  100.105    0.000  100.105    0.000 {built-in method multinomial}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-5>
Subject: Job 9441991: <Rock_level_interventionlow_0> in cluster <dcc> Done

Job <Rock_level_interventionlow_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Sat Mar 20 01:13:12 2021
Job was executed on host(s) <n-62-20-5>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sat Mar 20 13:08:41 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sat Mar 20 13:08:41 2021
Terminated at Sun Mar 21 01:04:02 2021
Results reported at Sun Mar 21 01:04:02 2021

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

    CPU time :                                   42801.41 sec.
    Max Memory :                                 6089 MB
    Average Memory :                             4377.25 MB
    Total Requested Memory :                     8192.00 MB
    Delta Memory :                               2103.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   42920 sec.
    Turnaround time :                            85850 sec.

The output (if any) is above this job summary.

