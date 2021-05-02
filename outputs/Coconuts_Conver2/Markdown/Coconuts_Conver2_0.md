
# Parameters

    Name :                      Coconuts_Conver2-0
    Main :                      CFagent
    Level :                     Levels.Coconuts
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


      58991151706 function calls (58701509511 primitive calls) in 86109.97 seconds

##    Ordered by: cumulative time
   List reduced from 512 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86109.967 86109.967 {built-in method builtins.exec}
                      1    4.511    4.511 86109.967 86109.967 <string>:1(<module>)
                      1  363.987  363.987 86105.456 86105.456 main.py:79(CFagent)
                9821001   39.422    0.000 32235.449    0.003 agent.py:29(learn)
                9821001  799.590    0.000 26926.058    0.003 learner.py:42(Qlearn)
                3273667   16.206    0.000 18949.851    0.006 game.py:41(step)
                3273667   20.171    0.000 18197.770    0.006 layers.py:718(step)
        324689436/35048932 1478.495    0.000 13129.141    0.000 module.py:866(_call_impl)
                3273667  309.623    0.000 12533.135    0.004 layers.py:17(step)
                3273667  357.235    0.000 12424.585    0.004 agent.py:54(_learn)
               25227931   72.273    0.000 12286.926    0.000 network.py:27(forward)
              327240605 1246.221    0.000 12192.589    0.000 layer.py:98(move)
               25227931  381.419    0.000 12043.734    0.000 container.py:117(forward)
                3273667  353.573    0.000 11532.181    0.004 agent.py:204(_learn)
                9821001   87.747    0.000 11423.700    0.001 optimizer.py:84(wrapper)
                9821001   43.343    0.000 10995.978    0.001 grad_mode.py:24(decorate_context)
                9821001  312.930    0.000 10854.227    0.001 adam.py:55(step)
                9821001 2230.007    0.000 10191.333    0.001 _functional.py:53(adam)
                3273667  103.257    0.000 8209.032    0.003 agent.py:117(_learn)
              327240605 1215.979    0.000 7398.515    0.000 layers.py:735(check)
                9821001   44.051    0.000 6743.775    0.001 tensor.py:195(backward)
                9821001   40.012    0.000 6698.208    0.001 __init__.py:68(backward)
                3273667  511.894    0.000 6419.328    0.002 agent.py:212(counterfact)
                9821001 6417.134    0.001 6417.134    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                7699270  214.795    0.000 6054.648    0.001 agent.py:49(__call__)
                3273667 4491.239    0.001 5641.343    0.002 replaybuffer.py:22(sample_data)
                3273668  495.860    0.000 5617.507    0.002 layers.py:684(update)
                3273667 4264.828    0.001 5371.323    0.002 replaybuffer.py:67(sample_data)
                3273667 2554.876    0.001 5113.133    0.002 agent.py:88(interveen)
                3273667 2671.763    0.001 5025.820    0.002 replaybuffer.py:28(teleporter_save_data)
               50455862  121.416    0.000 4308.568    0.000 conv.py:398(forward)
               50455862   90.802    0.000 4133.432    0.000 conv.py:390(_conv_forward)
               50455862 4042.630    0.000 4042.630    0.000 {built-in method conv2d}
               69136459  154.509    0.000 3477.092    0.000 linear.py:93(forward)
               39801903 3338.670    0.000 3338.670    0.000 {built-in method tensor}
               69136459   66.418    0.000 3249.623    0.000 functional.py:1737(linear)
               69136459 3167.866    0.000 3167.866    0.000 {built-in method torch._C._nn.linear}
               45831345 1841.462    0.000 3122.614    0.000 layer.py:151(update)
               32261366   24.403    0.000 3101.514    0.000 game.py:37(board)
                3273667 1977.877    0.001 3006.839    0.001 agent.py:67(modify)
              327240605  535.270    0.000 2696.300    0.000 layers.py:729(isFree)
              327240605 1631.873    0.000 2293.394    0.000 layers.py:471(check)
             2217355165 1805.479    0.000 2161.030    0.000 layer.py:95(isFree)
              146831959 2109.803    0.000 2109.803    0.000 {built-in method clone}
              183325352 2097.941    0.000 2097.941    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               94364390   92.213    0.000 1964.401    0.000 activation.py:713(forward)
               43709607 1947.815    0.000 1947.815    0.000 {built-in method cat}
                1160326   27.495    0.000 1910.966    0.002 agent.py:176(choose_action)
              327240605 1369.331    0.000 1903.885    0.000 layers.py:77(check)
               94364390   85.694    0.000 1872.188    0.000 functional.py:1364(leaky_relu)
              183325352 1832.277    0.000 1832.277    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                3273667   59.798    0.000 1800.407    0.001 agent.py:172(__call__)
               94364390 1769.297    0.000 1769.297    0.000 {built-in method torch._C._nn.leaky_relu}
               10972937   81.424    0.000 1715.009    0.000 agent.py:59(modify_board)
                3273667   58.876    0.000 1683.292    0.001 agent.py:112(__call__)
                9821001  250.409    0.000 1575.590    0.000 optimizer.py:189(zero_grad)
             5485525952 1058.915    0.000 1517.205    0.000 enum.py:646(__hash__)
                1638037   20.944    0.000 1250.254    0.001 layers.py:740(restart)
              329002431  277.537    0.000 1189.156    0.000 {built-in method builtins.any}
               91662676 1137.185    0.000 1137.185    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               10972937 1084.633    0.000 1084.633    0.000 {built-in method torch._C._nn.one_hot}
                1638037   10.525    0.000 1053.167    0.001 level.py:8(__init__)
                3273667  858.505    0.000 1052.078    0.000 replaybuffer.py:73(CF_save_data)
               91662676  978.465    0.000  978.465    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                1638037   71.164    0.000  958.837    0.001 levels.py:262(generate)
               91662676  947.963    0.000  947.963    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               91662676  938.124    0.000  938.124    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
             2605830104  743.860    0.000  911.620    0.000 layers.py:700(<genexpr>)
              327240605  697.734    0.000  905.391    0.000 layers.py:62(check)
                3273667   66.776    0.000  898.626    0.000 replaybuffer.py:18(stacker)
                3273667   66.927    0.000  864.312    0.000 replaybuffer.py:63(stacker)
               14610166  143.398    0.000  826.891    0.000 level.py:41(notUsed)
              327366800   64.326    0.000  799.369    0.000 {built-in method builtins.all}
              664434695  157.095    0.000  778.766    0.000 layers.py:690(<genexpr>)
                3273667  444.675    0.000  734.571    0.000 collector.py:46(collect)
             7673272062  731.929    0.000  731.929    0.000 layer.py:91(positions)
               91662676  723.761    0.000  723.761    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              947602568  717.192    0.000  717.192    0.000 layer.py:146(elements)
                7699270  228.514    0.000  628.452    0.000 exploration.py:53(softmaxer)
              327366800  418.302    0.000  617.545    0.000 layers.py:113(isDone)
              641638816  468.035    0.000  580.269    0.000 tensor.py:906(grad)
        6588962535/6588962532  496.887    0.000  563.597    0.000 {built-in method builtins.len}
              161078563  546.435    0.000  546.435    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
                9821001   17.602    0.000  521.317    0.000 loss.py:527(forward)
                9821001   39.594    0.000  503.715    0.000 functional.py:2898(mse_loss)
                6547334  180.006    0.000  480.838    0.000 random.py:315(sample)
             5485563279  458.297    0.000  458.297    0.000 {built-in method builtins.hash}
              327240605  301.902    0.000  451.686    0.000 layers.py:48(check)
               14610166   14.373    0.000  371.634    0.000 level.py:38(elementsIn)
              327240605  253.677    0.000  370.268    0.000 layers.py:23(check)
                1160326  300.423    0.000  344.210    0.000 agent.py:187(convert_values)
                9821001  333.766    0.000  333.766    0.000 {built-in method torch._C._nn.mse_loss}
               50455862   40.645    0.000  324.747    0.000 flatten.py:39(forward)
              336050524  199.629    0.000  311.739    0.000 layer.py:126(remove)
               19642002  309.115    0.000  309.115    0.000 {built-in method sum}
                6547336  297.881    0.000  297.881    0.000 {built-in method nonzero}
                9822097  294.127    0.000  294.127    0.000 {built-in method max}
               50455862  284.102    0.000  284.102    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
              428418597  185.857    0.000  251.641    0.000 layer.py:130(add)
              332398634  250.570    0.000  250.570    0.000 {built-in method torch._C._get_tracing_state}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9579169: <Coconuts_Conver2_0> in cluster <dcc> Done

Job <Coconuts_Conver2_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Tue Apr 27 02:44:07 2021
Job was executed on host(s) <n-62-20-14>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Thu Apr 29 10:49:21 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Thu Apr 29 10:49:21 2021
Terminated at Fri Apr 30 10:44:36 2021
Results reported at Fri Apr 30 10:44:36 2021

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

    CPU time :                                   85902.28 sec.
    Max Memory :                                 9481 MB
    Average Memory :                             6396.24 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               6903.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86116 sec.
    Turnaround time :                            288029 sec.

The output (if any) is above this job summary.

