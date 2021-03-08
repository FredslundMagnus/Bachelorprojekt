
# Parameters

    Name :                      gold_big-0
    Main :                      teleport
    Hours :                     10.0
    Batch :                     100
    Width :                     11
    Height :                    11
    Network1 :                  Networks.Teleporter
    Network2 :                  Networks.Mini
    Learner1 :                  Learners.Qlearn
    Learner2 :                  Learners.Qlearn
    Exploration1 :              Explorations.softmaxer
    Exploration2 :              Explorations.epsilonGreedy
    Layer blocks :              True
    Layer goal :                True
    Layer gold :                True
    Layer keys :                False
    Layer door :                False
    Layer holder :              False
    Layer putter :              False
    K :                         200000
    Epsilon cap :               0.2
    Softmax cap :               0.03
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


      12646780595 function calls (12539054444 primitive calls) in 35703.48 seconds

##    Ordered by: cumulative time
   List reduced from 465 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 35714.353 35714.353 {built-in method builtins.exec}
                      1    0.776    0.776 35714.353 35714.353 <string>:1(<module>)
                      1   93.128   93.128 35713.576 35713.576 main.py:10(teleport)
                3846252   13.865    0.000 11102.542    0.003 agent.py:26(learn)
                1923126  259.788    0.000 10556.051    0.005 collector.py:36(collect)
                9615630 9474.593    0.001 10270.291    0.001 {built-in method builtins.sum}
                3846252  293.075    0.000 9494.397    0.002 learner.py:42(Qlearn)
                1923126   71.087    0.000 6618.036    0.003 agent.py:50(_learn)
        121139531/13460543  501.448    0.000 4597.996    0.000 module.py:866(_call_impl)
                1923126   61.526    0.000 4458.852    0.002 agent.py:101(_learn)
                9614291   29.287    0.000 4288.695    0.000 network.py:24(forward)
                9614291  136.463    0.000 4199.169    0.000 container.py:117(forward)
                3846252   36.266    0.000 3983.302    0.001 optimizer.py:84(wrapper)
                3846252   17.437    0.000 3819.498    0.001 grad_mode.py:24(decorate_context)
                1923126    7.809    0.000 3811.839    0.002 game.py:21(step)
                3846252  108.297    0.000 3764.430    0.001 adam.py:55(step)
                3846252  776.441    0.000 3530.637    0.001 _functional.py:53(adam)
                1923126    9.101    0.000 3408.781    0.002 layers.py:212(step)
                1923126 1807.429    0.001 3256.309    0.002 replaybuffer.py:27(teleporter_save_data)
                1923126 1598.971    0.001 3005.766    0.002 agent.py:77(interveen)
                3844913   99.270    0.000 2845.139    0.001 agent.py:45(__call__)
                3846252   17.610    0.000 2344.828    0.001 tensor.py:195(backward)
                3846252   15.471    0.000 2326.650    0.001 __init__.py:68(backward)
                3846252 2224.165    0.001 2224.165    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                1923126  126.190    0.000 1943.688    0.001 layers.py:17(step)
              192312600  181.896    0.000 1801.205    0.000 layer.py:66(move)
               19228582   44.049    0.000 1552.350    0.000 conv.py:398(forward)
               19228582   25.901    0.000 1490.465    0.000 conv.py:390(_conv_forward)
               19228582 1464.564    0.000 1464.564    0.000 {built-in method conv2d}
                1923127  168.490    0.000 1442.733    0.001 layers.py:192(update)
                1923126  821.077    0.000 1410.160    0.001 agent.py:59(modify)
                1923126  663.161    0.000 1376.769    0.001 replaybuffer.py:23(sample_data)
               95716057 1190.191    0.000 1190.191    0.000 {built-in method clone}
               24996621   52.499    0.000 1189.388    0.000 linear.py:93(forward)
               24996621   21.733    0.000 1114.803    0.000 functional.py:1737(linear)
               24996621 1087.915    0.000 1087.915    0.000 {built-in method torch._C._nn.linear}
              192312600  149.690    0.000  926.856    0.000 layers.py:223(isFree)
                1923126   30.041    0.000  890.128    0.000 agent.py:96(__call__)
                5768039   38.553    0.000  847.774    0.000 agent.py:54(modify_board)
               11539524   22.979    0.000  828.200    0.000 tensor.py:575(__iter__)
               11539524  783.697    0.000  783.697    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
              617669133  685.374    0.000  777.166    0.000 layer.py:63(isFree)
               15383669  724.424    0.000  724.424    0.000 {built-in method cat}
               69232536  708.591    0.000  708.591    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               34610912   31.652    0.000  671.115    0.000 activation.py:713(forward)
               34610912   29.143    0.000  639.463    0.000 functional.py:1364(leaky_relu)
               69232536  636.433    0.000  636.433    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               34610912  603.654    0.000  603.654    0.000 {built-in method torch._C._nn.leaky_relu}
                1923126   36.626    0.000  580.697    0.000 replaybuffer.py:19(stacker)
                3846252   91.491    0.000  564.558    0.000 optimizer.py:189(zero_grad)
                8148144  545.876    0.000  545.876    0.000 {built-in method tensor}
                5768039  542.430    0.000  542.430    0.000 {built-in method torch._C._nn.one_hot}
              192312600  193.905    0.000  518.190    0.000 layers.py:229(check)
              192312700   52.175    0.000  477.771    0.000 {built-in method builtins.all}
              580515306  131.597    0.000  447.396    0.000 layers.py:197(<genexpr>)
                3846252    4.604    0.000  413.443    0.000 game.py:17(board)
               34616268  397.465    0.000  397.465    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                 653789    5.696    0.000  391.343    0.001 layers.py:233(restart)
                7692508  156.555    0.000  355.100    0.000 layer.py:90(update)
               34616268  344.989    0.000  344.989    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               34616268  330.691    0.000  330.691    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               34616268  325.486    0.000  325.486    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              101484096  323.429    0.000  323.429    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
                 653789    1.347    0.000  321.693    0.000 levels.py:8(__init__)
                 653789    3.113    0.000  320.346    0.000 level.py:8(__init__)
                 653789   62.023    0.000  310.563    0.000 levels.py:11(generate)
              192312700  196.308    0.000  298.727    0.000 layers.py:65(isDone)
                3844913  107.589    0.000  295.149    0.000 exploration.py:53(softmaxer)
              192312600  186.439    0.000  278.338    0.000 layers.py:50(check)
               34616268  257.389    0.000  257.389    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              242313930  167.146    0.000  208.071    0.000 tensor.py:906(grad)
                3846252    5.556    0.000  191.960    0.000 loss.py:527(forward)
                3846252   15.308    0.000  186.405    0.000 functional.py:2898(mse_loss)
              399083165  148.398    0.000  148.398    0.000 layer.py:85(elements)
                3230704   53.345    0.000  140.448    0.000 random.py:315(sample)
                 653789   66.598    0.000  129.170    0.000 levels.py:76(RFS)
             1488627700  128.537    0.000  128.537    0.000 layer.py:59(positions)
                3846252  121.790    0.000  121.790    0.000 {built-in method torch._C._nn.mse_loss}
              431044323   86.419    0.000  121.721    0.000 enum.py:646(__hash__)
               19228582   15.051    0.000  117.658    0.000 flatten.py:39(forward)
                3846828  108.392    0.000  108.392    0.000 {built-in method max}
        564537921/564537919   75.036    0.000  106.084    0.000 {built-in method builtins.len}
                5769378    8.275    0.000  105.788    0.000 tensor.py:525(__rsub__)
              192131264   76.509    0.000  102.813    0.000 layer.py:76(add)
               19228582  102.606    0.000  102.606    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
              132679055   97.850    0.000   97.850    0.000 {built-in method torch._C._get_tracing_state}
                5769378   95.965    0.000   95.965    0.000 {built-in method rsub}
              143133925   65.011    0.000   95.529    0.000 layer.py:72(remove)
                3844913   95.384    0.000   95.384    0.000 {built-in method multinomial}
                1923126    7.552    0.000   90.244    0.000 exploration.py:47(epsilonGreedy)
                3846252   85.236    0.000   85.236    0.000 {built-in method gather}
                3846252   15.529    0.000   83.566    0.000 __init__.py:28(_make_grads)
                7692504   19.192    0.000   82.869    0.000 profiler.py:615(__enter__)
              115888351   47.057    0.000   69.046    0.000 random.py:250(_randbelow_with_getrandbits)
                1923127   68.711    0.000   68.711    0.000 {built-in method nonzero}
                7692504   10.884    0.000   68.516    0.000 profiler.py:607(__init__)
                3846252   64.930    0.000   64.930    0.000 {built-in method ones_like}
                7692504   63.676    0.000   63.676    0.000 {built-in method torch._ops.profiler._record_function_enter}
              617669133   63.580    0.000   63.580    0.000 layer.py:125(isBlocking)
                4294981   62.922    0.000   62.922    0.000 {method 'long' of 'torch._C._TensorBase' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-5>
Subject: Job 9393240: <gold_big_0> in cluster <dcc> Done

Job <gold_big_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Mon Mar  8 01:58:30 2021
Job was executed on host(s) <n-62-20-5>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Mon Mar  8 01:58:32 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Mon Mar  8 01:58:32 2021
Terminated at Mon Mar  8 11:54:10 2021
Results reported at Mon Mar  8 11:54:10 2021

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

    CPU time :                                   35590.57 sec.
    Max Memory :                                 5107 MB
    Average Memory :                             3847.62 MB
    Total Requested Memory :                     8192.00 MB
    Delta Memory :                               3085.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   35825 sec.
    Turnaround time :                            35740 sec.

The output (if any) is above this job summary.

