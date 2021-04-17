
# Parameters

    Name :                      causal3_CF_convert5_2-0
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
    Cf convert :                5
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      49311891690 function calls (49023306827 primitive calls) in 86110.33 seconds

##    Ordered by: cumulative time
   List reduced from 494 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86110.329 86110.329 {built-in method builtins.exec}
                      1    4.651    4.651 86110.329 86110.329 <string>:1(<module>)
                      1  210.788  210.788 86105.678 86105.678 main.py:96(CFagent)
                9080085   35.867    0.000 34093.137    0.004 agent.py:29(learn)
                9080084  769.373    0.000 28854.103    0.003 learner.py:42(Qlearn)
        322720752/34137580 1268.365    0.000 14169.787    0.000 module.py:715(_call_impl)
               25057496   61.655    0.000 13369.387    0.001 network.py:24(forward)
               25057496  344.116    0.000 13163.873    0.001 container.py:115(forward)
                3026695  110.988    0.000 13095.011    0.004 agent.py:54(_learn)
                3026695   14.013    0.000 12481.095    0.004 game.py:35(step)
                9080084   58.850    0.000 12393.055    0.001 grad_mode.py:23(decorate_context)
                9080084  324.328    0.000 12227.939    0.001 adam.py:55(step)
                3026695  110.266    0.000 12215.510    0.004 agent.py:196(_learn)
                3026695   17.269    0.000 11741.375    0.004 layers.py:448(step)
                9080084 2233.776    0.000 10536.670    0.001 functional.py:53(adam)
                3026695 1045.795    0.000 9714.551    0.003 agent.py:204(counterfact)
                3026695   91.489    0.000 8724.252    0.003 agent.py:115(_learn)
                3026695 4111.815    0.001 8103.330    0.003 replaybuffer.py:28(teleporter_save_data)
                3026695  263.744    0.000 7763.782    0.003 layers.py:17(step)
              302669500  484.525    0.000 7472.233    0.000 layer.py:84(move)
                7987333  204.190    0.000 6794.475    0.001 agent.py:49(__call__)
                9080084   65.234    0.000 6747.941    0.001 tensor.py:181(backward)
                9080084   32.216    0.000 6682.706    0.001 __init__.py:68(backward)
                9080084 6410.574    0.001 6410.574    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                3026695 3426.069    0.001 6016.120    0.002 agent.py:86(interveen)
                3026695 3104.635    0.001 4696.903    0.002 replaybuffer.py:22(sample_data)
               50114992   87.859    0.000 4668.959    0.000 conv.py:422(forward)
               50114992   93.962    0.000 4547.762    0.000 conv.py:414(_conv_forward)
               50114992 4436.755    0.000 4436.755    0.000 {built-in method conv2d}
               69119098  158.282    0.000 4368.363    0.000 linear.py:92(forward)
               69119098  263.849    0.000 4137.838    0.000 functional.py:1669(linear)
              302669500  684.635    0.000 4131.559    0.000 layers.py:465(check)
               43153015 4034.174    0.000 4034.174    0.000 {built-in method tensor}
                3026695 2614.523    0.001 4027.053    0.001 replaybuffer.py:49(sample_data)
                3026696  322.442    0.000 3935.954    0.001 layers.py:419(update)
               36156488   26.434    0.000 3800.867    0.000 game.py:31(board)
                1936690   47.329    0.000 3531.522    0.002 agent.py:168(choose_action)
              229884572 3481.675    0.000 3481.675    0.000 {built-in method clone}
               48427128 1725.713    0.000 3040.357    0.000 layer.py:145(NoRock_update)
                3026695 1449.421    0.000 2960.504    0.001 agent.py:67(modify)
               69119098 2953.849    0.000 2953.849    0.000 {built-in method addmm}
               44307668 2804.786    0.000 2804.786    0.000 {built-in method cat}
              593232234 1633.508    0.000 2557.420    0.000 tensor.py:933(grad)
                9080084  237.952    0.000 2473.092    0.000 optimizer.py:167(zero_grad)
              302646623  476.118    0.000 2428.373    0.000 layers.py:459(isFree)
              169494900 2211.951    0.000 2211.951    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               94176594   77.973    0.000 2002.982    0.000 activation.py:713(forward)
             2237403524 1608.488    0.000 1952.255    0.000 layer.py:81(isFree)
               94176594  124.563    0.000 1925.009    0.000 functional.py:1292(leaky_relu)
              169494900 1846.710    0.000 1846.710    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               11014028   76.808    0.000 1842.108    0.000 agent.py:59(modify_board)
                3026694   46.258    0.000 1791.144    0.001 agent.py:164(__call__)
               94176594 1787.869    0.000 1787.869    0.000 {built-in method torch._C._nn.leaky_relu}
                3026695   47.052    0.000 1657.359    0.001 agent.py:110(__call__)
                3026695   74.805    0.000 1375.187    0.000 replaybuffer.py:18(stacker)
               84747450 1250.690    0.000 1250.690    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              769133685  427.866    0.000 1242.927    0.000 overrides.py:1070(has_torch_function)
                3026694   57.348    0.000 1199.187    0.000 replaybuffer.py:45(stacker)
                3952852   42.300    0.000 1158.044    0.000 layers.py:469(restart)
               11014028 1148.993    0.000 1148.993    0.000 {built-in method torch._C._nn.one_hot}
               84747450 1090.308    0.000 1090.308    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
             4311714843  740.728    0.000 1077.551    0.000 enum.py:646(__hash__)
                3026695  435.898    0.000 1076.143    0.000 replaybuffer.py:55(CF_save_data)
              243925294 1065.945    0.000 1065.945    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              302669500  626.218    0.000 1019.023    0.000 layers.py:233(check)
               22035561  131.184    0.000 1013.662    0.000 tensor.py:21(wrapped)
               84747450  985.482    0.000  985.482    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              302669500  569.928    0.000  955.188    0.000 layers.py:270(check)
               84747450  890.892    0.000  890.892    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              324705161  125.635    0.000  795.445    0.000 {built-in method builtins.all}
                3952852   20.511    0.000  793.434    0.000 level.py:8(__init__)
              859439647  325.725    0.000  780.858    0.000 {built-in method builtins.any}
                3026695  454.715    0.000  760.260    0.000 collector.py:54(collect)
             1074069799  734.531    0.000  734.531    0.000 layer.py:124(elements)
                7987333  259.550    0.000  725.169    0.000 exploration.py:53(softmaxer)
                1936690  461.240    0.000  696.534    0.000 agent.py:179(convert_values)
             1091625949  268.272    0.000  689.852    0.000 layers.py:425(<genexpr>)
               84747450  689.818    0.000  689.818    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                3952852   81.120    0.000  618.372    0.000 levels.py:164(generate)
               69119098  604.676    0.000  604.676    0.000 {method 't' of 'torch._C._TensorBase' objects}
                9080084   14.005    0.000  532.657    0.000 loss.py:445(forward)
                9080084   48.976    0.000  518.652    0.000 functional.py:2637(mse_loss)
              302669500  325.580    0.000  508.161    0.000 layers.py:257(check)
        5687099943/5687099940  387.236    0.000  507.031    0.000 {built-in method builtins.len}
               13959094  186.937    0.000  496.943    0.000 random.py:315(sample)
              302669500  310.849    0.000  489.407    0.000 layers.py:294(check)
             5213259164  454.089    0.000  454.089    0.000 layer.py:77(positions)
             1629421231  360.126    0.000  449.072    0.000 overrides.py:1083(<genexpr>)
                9080086  436.785    0.000  436.785    0.000 {built-in method nonzero}
                7905704   64.694    0.000  428.559    0.000 level.py:41(notUsed)
              302669500  268.235    0.000  395.764    0.000 layers.py:42(check)
                6054985  375.624    0.000  375.624    0.000 {method 'ne' of 'torch._C._TensorBase' objects}
               50114992   34.339    0.000  357.408    0.000 flatten.py:39(forward)
               14043469   68.032    0.000  351.266    0.000 tensor.py:506(__rsub__)
             4311749370  336.828    0.000  336.828    0.000 {built-in method builtins.hash}
                9080084  324.950    0.000  324.950    0.000 {built-in method torch._C._nn.mse_loss}
               50114992  323.069    0.000  323.069    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
               31622816   38.885    0.000  311.595    0.000 layer.py:58(restart)
              292771040  228.956    0.000  306.494    0.000 layer.py:104(remove)
               18160170  301.553    0.000  301.553    0.000 {built-in method sum}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-11-13>
Subject: Job 9496016: <causal3_CF_convert5_2_0> in cluster <dcc> Done

Job <causal3_CF_convert5_2_0> was submitted from host <n-62-27-19> by user <s183905> in cluster <dcc> at Mon Apr  5 20:05:18 2021
Job was executed on host(s) <n-62-11-13>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Mon Apr  5 20:48:17 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Mon Apr  5 20:48:17 2021
Terminated at Tue Apr  6 20:43:30 2021
Results reported at Tue Apr  6 20:43:30 2021

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

    CPU time :                                   86037.10 sec.
    Max Memory :                                 3401 MB
    Average Memory :                             3349.16 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               12983.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86113 sec.
    Turnaround time :                            88692 sec.

The output (if any) is above this job summary.

