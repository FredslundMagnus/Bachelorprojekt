
# Parameters

    Name :                      causal4_CF_convert2_2-0
    Main :                      CFagent
    Level :                     Levels.Causal4
    Hours :                     24.0
    Batch :                     100
    Width :                     9
    Height :                    9
    Network1 :                  Networks.Teleporter
    K1 :                        5000000
    Learner1 :                  Learners.Qlearn
    Exploration1 :              Explorations.softmaxer
    Gamma1 :                    0.98
    Network2 :                  Networks.Mini
    K2 :                        1000000
    Learner2 :                  Learners.Qlearn
    Exploration2 :              Explorations.epsilonGreedy
    Gamma2 :                    0.95
    Layer blocks :              True
    Layer goal :                True
    Layer gold :                True
    Layer keys :                True
    Layer door :                True
    Layer holder :              True
    Layer putter :              True
    Layer rock :                True
    Layer dirt :                True
    Layer diamond1 :            True
    Layer diamond2 :            True
    Layer diamond3 :            True
    Layer diamond4 :            True
    Layer reddoor :             True
    Layer redkeys :             True
    Layer bluedoor :            True
    Layer bluekeys :            True
    Layer pink1 :               True
    Layer pink2 :               True
    Layer pink3 :               True
    Layer brown1 :              True
    Layer brown2 :              True
    Layer brown3 :              True
    Epsilon cap :               0.2
    Softmax cap :               0.02
    Update :                    10000
    Reset chance :              0.001
    Modified done chance :      0.05
    Miss intervention cost :    -0.15
    Intervention cost :         -0.05
    Replay size :               100000
    Sample size :               50
    Cf convert :                2
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      60895980863 function calls (60568690084 primitive calls) in 86110.28 seconds

##    Ordered by: cumulative time
   List reduced from 508 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86110.284 86110.284 {built-in method builtins.exec}
                      1    5.460    5.460 86110.284 86110.284 <string>:1(<module>)
                      1  316.366  316.366 86104.824 86104.824 main.py:96(CFagent)
               10678575   47.771    0.000 27226.367    0.003 agent.py:29(learn)
               10678553  691.098    0.000 21922.669    0.002 learner.py:42(Qlearn)
                3559525   22.156    0.000 19777.290    0.006 game.py:35(step)
                3559525   23.427    0.000 18903.248    0.005 layers.py:448(step)
                3559525  362.800    0.000 13319.921    0.004 layers.py:17(step)
              355730807  957.617    0.000 12921.149    0.000 layer.py:84(move)
        366428240/39139152 1565.870    0.000 12487.251    0.000 module.py:866(_call_impl)
               28460599   82.484    0.000 11640.868    0.000 network.py:24(forward)
                3559525  964.913    0.000 11510.643    0.003 agent.py:204(counterfact)
               28460599  384.562    0.000 11358.296    0.000 container.py:117(forward)
                3559525  447.023    0.000 10639.907    0.003 agent.py:54(_learn)
                3559525  440.721    0.000 9665.858    0.003 agent.py:196(_learn)
               10678553  100.623    0.000 8403.685    0.001 optimizer.py:84(wrapper)
               10678553   60.093    0.000 7965.948    0.001 grad_mode.py:24(decorate_context)
               10678553  363.593    0.000 7790.415    0.001 adam.py:55(step)
              355730807 1166.925    0.000 7234.312    0.000 layers.py:465(check)
               10678553 1627.673    0.000 7045.778    0.001 _functional.py:53(adam)
                3559525 5522.073    0.002 6932.514    0.002 replaybuffer.py:22(sample_data)
                3559525  117.957    0.000 6847.028    0.002 agent.py:115(_learn)
                8883657  287.942    0.000 6060.062    0.001 agent.py:49(__call__)
                3559525 4726.902    0.001 5946.958    0.002 replaybuffer.py:49(sample_data)
               56036706 5920.483    0.000 5920.483    0.000 {built-in method tensor}
               10678553   50.040    0.000 5781.459    0.001 tensor.py:195(backward)
               10678553   53.409    0.000 5729.779    0.001 __init__.py:68(backward)
               47864854   31.907    0.000 5708.755    0.000 game.py:31(board)
                3559526  399.861    0.000 5520.095    0.002 layers.py:419(update)
               71190510 3180.798    0.000 5476.580    0.000 layer.py:129(update)
               10678553 5450.932    0.001 5450.932    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                3559525 2568.897    0.001 4386.911    0.001 replaybuffer.py:28(teleporter_save_data)
                3559525 1889.535    0.001 4258.628    0.001 agent.py:86(interveen)
               56921198  137.044    0.000 4214.815    0.000 conv.py:398(forward)
              355449166  756.934    0.000 4080.480    0.000 layers.py:459(isFree)
               56921198   88.784    0.000 4010.204    0.000 conv.py:390(_conv_forward)
               56921198 3921.420    0.000 3921.420    0.000 {built-in method conv2d}
             3444145434 2778.358    0.000 3323.546    0.000 layer.py:81(isFree)
               78262747  172.390    0.000 3175.775    0.000 linear.py:93(forward)
               78262747   68.721    0.000 2913.439    0.000 functional.py:1737(linear)
               78262747 2828.816    0.000 2828.816    0.000 {built-in method torch._C._nn.linear}
                1779361   38.770    0.000 2542.543    0.001 agent.py:168(choose_action)
                3559525 1450.366    0.000 2441.490    0.001 agent.py:67(modify)
               51597847 2163.275    0.000 2163.275    0.000 {built-in method cat}
              170305901 1772.601    0.000 1772.601    0.000 {built-in method clone}
               12443182   86.055    0.000 1689.636    0.000 agent.py:59(modify_board)
                3559503   80.883    0.000 1686.207    0.000 agent.py:164(__call__)
              106723346   97.704    0.000 1669.031    0.000 activation.py:713(forward)
              106723346   92.743    0.000 1571.328    0.000 functional.py:1364(leaky_relu)
                3559525   77.063    0.000 1570.615    0.000 agent.py:110(__call__)
             5841448717 1050.061    0.000 1481.785    0.000 enum.py:646(__hash__)
              106723346 1460.074    0.000 1460.074    0.000 {built-in method torch._C._nn.leaky_relu}
             1172577171 1397.900    0.000 1397.900    0.000 layer.py:124(elements)
              199332960 1382.439    0.000 1382.439    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              355730807  829.793    0.000 1250.492    0.000 layers.py:270(check)
               10678553  230.765    0.000 1234.776    0.000 optimizer.py:189(zero_grad)
              199332960 1212.323    0.000 1212.323    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                3371197   44.482    0.000 1194.571    0.000 layers.py:469(restart)
                3559525   93.831    0.000 1119.386    0.000 replaybuffer.py:18(stacker)
               12443182 1113.222    0.000 1113.222    0.000 {built-in method torch._C._nn.one_hot}
              355730807  675.314    0.000 1107.078    0.000 layers.py:233(check)
              355730807  833.723    0.000 1066.577    0.000 layers.py:67(check)
              355952600  168.960    0.000  965.340    0.000 {built-in method builtins.all}
                3559503   91.346    0.000  941.798    0.000 replaybuffer.py:45(stacker)
             1906650698  490.534    0.000  839.416    0.000 layers.py:425(<genexpr>)
              355730807  654.782    0.000  817.175    0.000 layers.py:56(check)
                3371197   20.956    0.000  813.798    0.000 level.py:8(__init__)
               99666480  796.798    0.000  796.798    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                3559525  326.748    0.000  773.972    0.000 replaybuffer.py:55(CF_save_data)
             8024739362  726.858    0.000  726.858    0.000 layer.py:77(positions)
               99666480  712.629    0.000  712.629    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                3371197  121.974    0.000  656.429    0.000 levels.py:199(generate)
               99666480  645.756    0.000  645.756    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               99666480  641.435    0.000  641.435    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              355730807  424.013    0.000  641.242    0.000 layers.py:294(check)
        8647367401/8647367398  555.971    0.000  624.850    0.000 {built-in method builtins.len}
               13861444  240.166    0.000  614.492    0.000 random.py:315(sample)
                8883657  220.616    0.000  613.423    0.000 exploration.py:53(softmaxer)
              355730807  383.036    0.000  597.319    0.000 layers.py:257(check)
              697665444  471.576    0.000  583.218    0.000 tensor.py:906(grad)
                3559525  324.492    0.000  549.148    0.000 collector.py:54(collect)
                1779361  436.233    0.000  512.500    0.000 agent.py:179(convert_values)
               10678553   19.673    0.000  507.757    0.000 loss.py:527(forward)
              355730807  346.492    0.000  496.617    0.000 layers.py:42(check)
               10678553   49.679    0.000  488.085    0.000 functional.py:2898(mse_loss)
               99666480  478.485    0.000  478.485    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
               10678576  456.974    0.000  456.974    0.000 {built-in method nonzero}
             5841489180  431.732    0.000  431.732    0.000 {built-in method builtins.hash}
                6742394   51.470    0.000  418.899    0.000 level.py:41(notUsed)
              186308586  386.135    0.000  386.135    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              317564112  249.383    0.000  353.450    0.000 layer.py:104(remove)
               33711970   50.123    0.000  325.031    0.000 layer.py:58(restart)
               71190510  319.477    0.000  319.477    0.000 layer.py:141(<listcomp>)
              515941774  226.725    0.000  317.205    0.000 layer.py:108(add)
               56921198   61.889    0.000  298.961    0.000 flatten.py:39(forward)
              429651318  198.845    0.000  296.798    0.000 random.py:250(_randbelow_with_getrandbits)
               10678553  294.839    0.000  294.839    0.000 {built-in method torch._C._nn.mse_loss}
             2739414916  291.526    0.000  291.526    0.000 layer.py:181(isBlocking)
               10679796  267.398    0.000  267.398    0.000 {built-in method max}
               16017439   29.320    0.000  254.492    0.000 tensor.py:525(__rsub__)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-10>
Subject: Job 9496007: <causal4_CF_convert2_2_0> in cluster <dcc> Done

Job <causal4_CF_convert2_2_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Mon Apr  5 20:00:35 2021
Job was executed on host(s) <n-62-20-10>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Mon Apr  5 21:10:50 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Mon Apr  5 21:10:50 2021
Terminated at Tue Apr  6 21:06:15 2021
Results reported at Tue Apr  6 21:06:15 2021

Your job looked like:

------------------------------------------------------------
# LSBATCH: User input
#!/bin/sh
#BSUB -q hpc
#BSUB -q gpuv100
#BSUB -gpu "num=1:mode=exclusive_process"
#BSUB -n 1
#BSUB -R "rusage[mem=16G]"
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

    CPU time :                                   85898.95 sec.
    Max Memory :                                 9932 MB
    Average Memory :                             6497.39 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               6452.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86125 sec.
    Turnaround time :                            90340 sec.

The output (if any) is above this job summary.

