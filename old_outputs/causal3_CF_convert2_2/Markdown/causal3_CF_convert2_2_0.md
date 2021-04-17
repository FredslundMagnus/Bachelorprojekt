
# Parameters

    Name :                      causal3_CF_convert2_2-0
    Main :                      CFagent
    Level :                     Levels.Causal3
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


      46923781559 function calls (46653497228 primitive calls) in 86109.79 seconds

##    Ordered by: cumulative time
   List reduced from 494 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86109.788 86109.788 {built-in method builtins.exec}
                      1    4.540    4.540 86109.788 86109.788 <string>:1(<module>)
                      1  207.312  207.312 86105.248 86105.248 main.py:96(CFagent)
                8487672   34.061    0.000 32998.921    0.004 agent.py:29(learn)
                8487672  748.746    0.000 27906.097    0.003 learner.py:42(Qlearn)
        302236940/31954300 1245.170    0.000 13773.861    0.000 module.py:715(_call_impl)
               23466628   61.739    0.000 12998.660    0.001 network.py:24(forward)
               23466628  331.365    0.000 12790.289    0.001 container.py:115(forward)
                2829224  105.051    0.000 12686.722    0.004 agent.py:54(_learn)
                2829224   15.447    0.000 12545.388    0.004 game.py:35(step)
                8487672   52.655    0.000 12042.525    0.001 grad_mode.py:23(decorate_context)
                8487672  305.733    0.000 11891.723    0.001 adam.py:55(step)
                2829224  103.176    0.000 11838.694    0.004 agent.py:196(_learn)
                2829224   17.358    0.000 11832.617    0.004 layers.py:448(step)
                8487672 2196.605    0.000 10274.073    0.001 functional.py:53(adam)
                2829224 1086.056    0.000 9613.660    0.003 agent.py:204(counterfact)
                2829224 4503.724    0.002 8812.387    0.003 replaybuffer.py:28(teleporter_save_data)
                2829224   85.104    0.000 8421.132    0.003 agent.py:115(_learn)
                2829224  253.477    0.000 7643.380    0.003 layers.py:17(step)
              282763412  458.107    0.000 7360.549    0.000 layer.py:84(move)
                7488300  193.264    0.000 6615.184    0.001 agent.py:49(__call__)
                8487672   52.618    0.000 6438.277    0.001 tensor.py:181(backward)
                8487672   30.564    0.000 6385.659    0.001 __init__.py:68(backward)
                2829224 3766.157    0.001 6279.068    0.002 agent.py:86(interveen)
                8487672 6119.843    0.001 6119.843    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                2829224 3295.960    0.001 4863.790    0.002 replaybuffer.py:22(sample_data)
               46933256   81.743    0.000 4539.193    0.000 conv.py:422(forward)
               46933256   91.447    0.000 4422.395    0.000 conv.py:414(_conv_forward)
               46933256 4313.946    0.000 4313.946    0.000 {built-in method conv2d}
               64741436  150.743    0.000 4236.443    0.000 linear.py:92(forward)
                2829225  320.368    0.000 4147.023    0.001 layers.py:419(update)
                2829224 2740.570    0.001 4121.894    0.001 replaybuffer.py:49(sample_data)
              282763412  666.214    0.000 4019.111    0.000 layers.py:465(check)
               64741436  252.339    0.000 4012.191    0.000 functional.py:1669(linear)
               40640443 3876.042    0.000 3876.042    0.000 {built-in method tensor}
              235635901 3756.392    0.000 3756.392    0.000 {built-in method clone}
               34080949   26.378    0.000 3647.847    0.000 game.py:31(board)
                1832208   47.204    0.000 3571.857    0.002 agent.py:168(choose_action)
               45267592 1699.434    0.000 2997.825    0.000 layer.py:145(NoRock_update)
                2829224 1427.825    0.001 2903.105    0.001 agent.py:67(modify)
               64741436 2864.064    0.000 2864.064    0.000 {built-in method addmm}
               41438988 2754.023    0.000 2754.023    0.000 {built-in method cat}
              554527988 1573.851    0.000 2471.414    0.000 tensor.py:933(grad)
              282760226  459.354    0.000 2448.529    0.000 layers.py:459(isFree)
                8487672  223.967    0.000 2402.638    0.000 optimizer.py:167(zero_grad)
              158436544 2163.543    0.000 2163.543    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
             1998413712 1643.088    0.000 1989.175    0.000 layer.py:81(isFree)
               88208064   76.210    0.000 1933.048    0.000 activation.py:713(forward)
               88208064  114.131    0.000 1856.837    0.000 functional.py:1292(leaky_relu)
              158436544 1814.129    0.000 1814.129    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               10317524   79.384    0.000 1805.386    0.000 agent.py:59(modify_board)
                2829224   46.031    0.000 1745.464    0.001 agent.py:164(__call__)
               88208064 1730.107    0.000 1730.107    0.000 {built-in method torch._C._nn.leaky_relu}
                2829224   46.781    0.000 1615.174    0.001 agent.py:110(__call__)
                2829224   73.301    0.000 1353.010    0.000 replaybuffer.py:18(stacker)
                3956503   43.005    0.000 1221.610    0.000 layers.py:469(restart)
              719128878  414.888    0.000 1218.224    0.000 overrides.py:1070(has_torch_function)
                2829224   53.788    0.000 1173.338    0.000 replaybuffer.py:45(stacker)
               79218272 1162.288    0.000 1162.288    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               10317524 1126.380    0.000 1126.380    0.000 {built-in method torch._C._nn.one_hot}
              248782649 1120.087    0.000 1120.087    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
                2829224  457.927    0.000 1110.096    0.000 replaybuffer.py:55(CF_save_data)
             4051156833  767.394    0.000 1075.695    0.000 enum.py:646(__hash__)
               79218272 1068.688    0.000 1068.688    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              282763412  627.290    0.000 1005.038    0.000 layers.py:270(check)
               20641790  124.682    0.000 1002.042    0.000 tensor.py:21(wrapped)
               79218272  969.906    0.000  969.906    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              303564290  148.326    0.000  951.061    0.000 {built-in method builtins.all}
              282763412  547.309    0.000  926.191    0.000 layers.py:233(check)
               79218272  872.034    0.000  872.034    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                3956503   21.059    0.000  838.042    0.000 level.py:8(__init__)
             1461140780  382.857    0.000  823.633    0.000 layers.py:425(<genexpr>)
                1832208  513.286    0.000  783.364    0.000 agent.py:179(convert_values)
              803674883  315.148    0.000  767.170    0.000 {built-in method builtins.any}
                2829224  440.381    0.000  738.124    0.000 collector.py:54(collect)
             1028286724  728.525    0.000  728.525    0.000 layer.py:124(elements)
                7488300  251.870    0.000  705.267    0.000 exploration.py:53(softmaxer)
               79218272  675.755    0.000  675.755    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                3956503   86.178    0.000  657.114    0.000 levels.py:164(generate)
               64741436  586.315    0.000  586.315    0.000 {method 't' of 'torch._C._TensorBase' objects}
                8487672   12.117    0.000  510.581    0.000 loss.py:445(forward)
                8487672   46.023    0.000  498.464    0.000 functional.py:2637(mse_loss)
               13571454  186.247    0.000  492.789    0.000 random.py:315(sample)
              282763412  310.927    0.000  485.379    0.000 layers.py:257(check)
        5261948479/5261948476  368.329    0.000  484.659    0.000 {built-in method builtins.len}
              282763412  291.565    0.000  459.509    0.000 layers.py:294(check)
                7913006   68.605    0.000  456.559    0.000 level.py:41(notUsed)
             1523640234  361.224    0.000  446.462    0.000 overrides.py:1083(<genexpr>)
             4824402039  435.233    0.000  435.233    0.000 layer.py:77(positions)
                8487673  430.970    0.000  430.970    0.000 {built-in method nonzero}
              282763412  268.358    0.000  401.049    0.000 layers.py:42(check)
                5659944  378.115    0.000  378.115    0.000 {method 'ne' of 'torch._C._TensorBase' objects}
               46933256   38.359    0.000  346.902    0.000 flatten.py:39(forward)
               13149104   66.105    0.000  338.804    0.000 tensor.py:506(__rsub__)
               31652024   40.339    0.000  328.942    0.000 layer.py:58(restart)
                8487672  318.038    0.000  318.038    0.000 {built-in method torch._C._nn.mse_loss}
               46933256  308.544    0.000  308.544    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
             4051189120  308.307    0.000  308.307    0.000 {built-in method builtins.hash}
              309729092  302.947    0.000  302.947    0.000 {built-in method torch._C._get_tracing_state}
               16975344  295.329    0.000  295.329    0.000 {built-in method sum}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-14>
Subject: Job 9496013: <causal3_CF_convert2_2_0> in cluster <dcc> Done

Job <causal3_CF_convert2_2_0> was submitted from host <n-62-27-19> by user <s183905> in cluster <dcc> at Mon Apr  5 20:05:18 2021
Job was executed on host(s) <n-62-20-14>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Mon Apr  5 20:36:22 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Mon Apr  5 20:36:22 2021
Terminated at Tue Apr  6 20:31:35 2021
Results reported at Tue Apr  6 20:31:35 2021

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

    CPU time :                                   85899.16 sec.
    Max Memory :                                 3402 MB
    Average Memory :                             3349.59 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               12982.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86113 sec.
    Turnaround time :                            87977 sec.

The output (if any) is above this job summary.

