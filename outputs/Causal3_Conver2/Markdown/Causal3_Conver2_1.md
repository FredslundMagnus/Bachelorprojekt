
# Parameters

    Name :                      Causal3_Conver2-1
    Main :                      CFagent
    Level :                     Levels.Causal3
    Failed actions chance :     0.0
    Hours :                     24.0
    Batch :                     100
    Width :                     9
    Height :                    9
    Graphmode :                 GraphMode.UCB1
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
    Layer greendown :           True
    Layer greenup :             True
    Layer greenstar :           True
    Layer yellowstar :          True
    Layer bluestar :            True
    Layer coconut :             True
    Layer monster :             True
    Layer greencross :          True
    Layer bluecross :           True
    Layer redcross :            True
    Layer purplecross :         True
    Epsilon cap :               0.2
    Softmax cap :               0.02
    Update :                    10000
    Reset chance :              0.002
    Modified done chance :      0.05
    Miss intervention cost :    -0.15
    Intervention cost :         -0.05
    Replay size :               100000
    Sample size :               50
    Cf convert :                2
    Counterfacts :              1
    Topn :                      3
    Random counterfacts :       False
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      71285852421 function calls (70919123498 primitive calls) in 86109.25 seconds

##    Ordered by: cumulative time
   List reduced from 509 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86109.248 86109.248 {built-in method builtins.exec}
                      1    3.876    3.876 86109.248 86109.248 <string>:1(<module>)
                      1  352.778  352.778 86105.372 86105.372 main.py:79(CFagent)
               11406495   41.799    0.000 27337.290    0.002 agent.py:29(learn)
               11406487  684.370    0.000 22440.343    0.002 learner.py:42(Qlearn)
                3802165   15.839    0.000 19111.984    0.005 game.py:41(step)
                3802165   21.263    0.000 18336.359    0.005 layers.py:718(step)
        409961710/43234478 1622.034    0.000 12937.226    0.000 module.py:866(_call_impl)
               31827991   88.066    0.000 12098.134    0.000 network.py:27(forward)
               31827991  398.215    0.000 11807.244    0.000 container.py:117(forward)
                3802165  333.889    0.000 11163.123    0.003 layers.py:17(step)
              380216500  652.456    0.000 10797.177    0.000 layer.py:98(move)
                3802165  342.579    0.000 10583.618    0.003 agent.py:54(_learn)
                3802165 1022.314    0.000 9995.508    0.003 agent.py:212(counterfact)
                3802165  340.703    0.000 9737.597    0.003 agent.py:204(_learn)
               11406487   93.666    0.000 8895.373    0.001 optimizer.py:84(wrapper)
               11406487   47.691    0.000 8460.506    0.001 grad_mode.py:24(decorate_context)
               11406487  332.101    0.000 8306.312    0.001 adam.py:55(step)
               11406487 1724.753    0.000 7591.141    0.001 _functional.py:53(adam)
                3802166  555.297    0.000 7123.088    0.002 layers.py:684(update)
                3802165  102.513    0.000 6950.716    0.002 agent.py:117(_learn)
              380216500 1390.282    0.000 6459.359    0.000 layers.py:735(check)
               10208791  226.888    0.000 6319.064    0.001 agent.py:49(__call__)
                3802165 3323.782    0.001 5946.854    0.002 replaybuffer.py:28(teleporter_save_data)
               11406487   52.857    0.000 5822.839    0.001 tensor.py:195(backward)
               11406487   46.273    0.000 5768.339    0.001 __init__.py:68(backward)
                3802165 4549.785    0.001 5623.602    0.001 replaybuffer.py:22(sample_data)
               11406487 5503.621    0.000 5503.621    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
                3802165 4384.632    0.001 5437.844    0.001 replaybuffer.py:67(sample_data)
                3802165 2939.472    0.001 5284.296    0.001 agent.py:88(interveen)
               54699386 4598.604    0.000 4598.604    0.000 {built-in method tensor}
               45993576   27.829    0.000 4394.275    0.000 game.py:37(board)
               63655982  140.061    0.000 4336.853    0.000 conv.py:398(forward)
               63655982   81.204    0.000 4132.865    0.000 conv.py:390(_conv_forward)
               63655982 4051.661    0.000 4051.661    0.000 {built-in method conv2d}
               60834648 1992.425    0.000 3617.589    0.000 layer.py:167(NoRock_update)
                2608391   49.691    0.000 3407.968    0.001 agent.py:176(choose_action)
               87879643  175.578    0.000 3332.534    0.000 linear.py:93(forward)
              380216500  634.264    0.000 3110.831    0.000 layers.py:729(isFree)
               87879643   73.175    0.000 3071.463    0.000 functional.py:1737(linear)
               87879643 2980.065    0.000 2980.065    0.000 {built-in method torch._C._nn.linear}
                3802165 1840.329    0.000 2758.209    0.001 agent.py:67(modify)
              262349610 2505.689    0.000 2505.689    0.000 {built-in method clone}
             2850828487 2026.731    0.000 2476.567    0.000 layer.py:95(isFree)
               52032566 1779.298    0.000 1779.298    0.000 {built-in method cat}
               14010956   86.988    0.000 1766.363    0.000 agent.py:59(modify_board)
              119707634   94.918    0.000 1752.190    0.000 activation.py:713(forward)
                5363537   58.959    0.000 1717.668    0.000 layers.py:740(restart)
              119707634   98.538    0.000 1657.271    0.000 functional.py:1364(leaky_relu)
                3802157   53.093    0.000 1640.337    0.000 agent.py:172(__call__)
                3802165 1218.069    0.000 1590.373    0.000 replaybuffer.py:73(CF_save_data)
                3802165   51.457    0.000 1543.097    0.000 agent.py:112(__call__)
              119707634 1539.310    0.000 1539.310    0.000 {built-in method torch._C._nn.leaky_relu}
              212921080 1471.991    0.000 1471.991    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
             5736371407 1016.138    0.000 1457.308    0.000 enum.py:646(__hash__)
              378655229  339.617    0.000 1382.094    0.000 {built-in method builtins.any}
              380216500  840.644    0.000 1344.231    0.000 layers.py:286(check)
              380216600  204.517    0.000 1339.822    0.000 {built-in method builtins.all}
              212921080 1310.092    0.000 1310.092    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               11406487  233.547    0.000 1309.915    0.000 optimizer.py:189(zero_grad)
              380216500  741.945    0.000 1250.620    0.000 layers.py:246(check)
                5363537   27.995    0.000 1219.759    0.000 level.py:8(__init__)
             2081600791  555.120    0.000 1181.633    0.000 layers.py:690(<genexpr>)
               14010956 1160.557    0.000 1160.557    0.000 {built-in method torch._C._nn.one_hot}
             3373677567  855.308    0.000 1042.477    0.000 layers.py:700(<genexpr>)
                5363537  111.241    0.000  952.967    0.000 levels.py:164(generate)
              106460540  926.152    0.000  926.152    0.000 {method 'add' of 'torch._C._TensorBase' objects}
             1404483395  917.970    0.000  917.970    0.000 layer.py:146(elements)
                3802165   65.457    0.000  805.635    0.000 replaybuffer.py:18(stacker)
                3802157   64.139    0.000  788.931    0.000 replaybuffer.py:63(stacker)
              106460540  742.679    0.000  742.679    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
             7327116109  698.942    0.000  698.942    0.000 layer.py:91(positions)
              106460540  694.489    0.000  694.489    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               10727074   99.183    0.000  693.976    0.000 level.py:41(notUsed)
              106460540  691.450    0.000  691.450    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
        8635495735/8635495732  590.552    0.000  662.593    0.000 {built-in method builtins.len}
                2608391  569.721    0.000  639.431    0.000 agent.py:187(convert_values)
               10208791  236.373    0.000  632.042    0.000 exploration.py:53(softmaxer)
               18331404  236.694    0.000  622.805    0.000 random.py:315(sample)
              380216500  388.765    0.000  613.509    0.000 layers.py:273(check)
              745223864  488.662    0.000  606.548    0.000 tensor.py:906(grad)
              380216500  375.700    0.000  593.971    0.000 layers.py:313(check)
                3802165  339.864    0.000  575.497    0.000 collector.py:46(collect)
              280162723  555.317    0.000  555.317    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              380216500  357.519    0.000  540.479    0.000 layers.py:48(check)
              106460540  524.597    0.000  524.597    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
               11406487   15.348    0.000  479.829    0.000 loss.py:527(forward)
               11406487   43.903    0.000  464.481    0.000 functional.py:2898(mse_loss)
             5736414670  441.177    0.000  441.177    0.000 {built-in method builtins.hash}
               42908296   52.635    0.000  424.424    0.000 layer.py:69(restart)
              380216500  280.671    0.000  416.927    0.000 layers.py:23(check)
              219524778  265.388    0.000  400.678    0.000 layers.py:113(isDone)
              643837481  259.025    0.000  357.386    0.000 layer.py:130(add)
              519262633  231.478    0.000  337.079    0.000 random.py:250(_randbelow_with_getrandbits)
              372902766  213.011    0.000  310.632    0.000 layer.py:126(remove)
               63655982   46.146    0.000  296.587    0.000 flatten.py:39(forward)
               11406487  284.986    0.000  284.986    0.000 {built-in method torch._C._nn.mse_loss}
             3450423356  279.499    0.000  279.499    0.000 {method 'random' of '_random.Random' objects}
               10727074   11.719    0.000  278.075    0.000 level.py:38(elementsIn)
                7604332  276.968    0.000  276.968    0.000 {built-in method nonzero}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9579158: <Causal3_Conver2_1> in cluster <dcc> Done

Job <Causal3_Conver2_1> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Tue Apr 27 02:44:05 2021
Job was executed on host(s) <n-62-11-13>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Tue Apr 27 05:40:50 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Tue Apr 27 05:40:50 2021
Terminated at Wed Apr 28 05:36:03 2021
Results reported at Wed Apr 28 05:36:03 2021

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

    CPU time :                                   86042.07 sec.
    Max Memory :                                 3442 MB
    Average Memory :                             3417.13 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               12942.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86112 sec.
    Turnaround time :                            96718 sec.

The output (if any) is above this job summary.

