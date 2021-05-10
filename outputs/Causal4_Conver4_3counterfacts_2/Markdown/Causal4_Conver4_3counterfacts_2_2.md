
# Parameters

    Name :                      Causal4_Conver4_3counterfacts_2-2
    Main :                      Load_Cfagent
    Level :                     Levels.Causal4
    Failed actions chance :     0
    Use model :                 True
    Depth :                     3
    Model explore :             1000000
    Samples :                   5
    Hours :                     11.0
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
    Layer super1 :              True
    Layer super2 :              True
    Layer super3 :              True
    Layer super4 :              True
    Layer super5 :              True
    Layer super6 :              True
    Layer super7 :              True
    Epsilon cap :               0.2
    Softmax cap :               0.02
    Update :                    10000
    Reset chance :              0.002
    Modified done chance :      0.05
    Miss intervention cost :    -0.15
    Intervention cost :         -0.05
    Replay size :               100000
    Sample size :               50
    Cf convert :                4
    Counterfacts :              3
    Topn :                      5
    Random counterfacts :       False
    Num :                       2
    Load name :                 Causal4_Conver4_3counterfacts
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      64659739021 function calls (64310640640 primitive calls) in 86120.83 seconds

##    Ordered by: cumulative time
   List reduced from 436 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86120.834 86120.834 {built-in method builtins.exec}
                      1    4.313    4.313 86120.834 86120.834 <string>:1(<module>)
                      1  283.121  283.121 86116.521 86116.521 main.py:109(Load_Cfagent)
                2538667 3026.656    0.001 27361.504    0.011 agent.py:212(counterfact)
                7616001   28.717    0.000 19229.091    0.003 agent.py:29(learn)
                2538667   10.145    0.000 17737.960    0.007 game.py:42(step)
                2538667   15.282    0.000 17150.344    0.007 layers.py:827(step)
                7616001  485.427    0.000 15684.806    0.002 learner.py:42(Qlearn)
        386649080/37553520 1621.421    0.000 12785.209    0.000 module.py:866(_call_impl)
               29937519   81.297    0.000 12113.227    0.000 network.py:28(forward)
               29937519  378.443    0.000 11825.955    0.000 container.py:117(forward)
              106727378 11371.250    0.000 11371.250    0.000 {built-in method tensor}
              101128022   58.990    0.000 11274.296    0.000 game.py:38(board)
                2538667  225.259    0.000 10770.152    0.004 layers.py:17(step)
              253652862  741.651    0.000 10520.765    0.000 layer.py:106(move)
                6087244  120.323    0.000 8489.963    0.001 agent.py:176(choose_action)
                2538667  270.015    0.000 7465.442    0.003 agent.py:54(_learn)
               11156940  294.722    0.000 7268.146    0.001 agent.py:49(__call__)
                2538667  267.225    0.000 6862.019    0.003 agent.py:204(_learn)
              253652862 1297.582    0.000 6512.688    0.000 layers.py:844(check)
                2538667  396.946    0.000 6344.189    0.002 layers.py:793(update)
              101546660 3514.318    0.000 6203.569    0.000 layer.py:159(update)
                7616001   61.488    0.000 6118.414    0.001 optimizer.py:84(wrapper)
                7616001   33.671    0.000 5832.112    0.001 grad_mode.py:24(decorate_context)
                7616001  244.688    0.000 5724.621    0.001 adam.py:55(step)
                7616001 1190.874    0.000 5211.251    0.001 _functional.py:53(adam)
                2538667   78.709    0.000 4856.507    0.002 agent.py:117(_learn)
                2538667 3823.687    0.002 4607.270    0.002 replaybuffer.py:22(sample_data)
                2538667 3806.026    0.001 4567.372    0.002 replaybuffer.py:67(sample_data)
               59875038  136.416    0.000 4363.159    0.000 conv.py:398(forward)
               59875038   91.507    0.000 4157.720    0.000 conv.py:390(_conv_forward)
                7616001   26.660    0.000 4101.563    0.001 tensor.py:195(backward)
                7616001   29.710    0.000 4073.734    0.001 __init__.py:68(backward)
               59875038 4066.213    0.000 4066.213    0.000 {built-in method conv2d}
                7616001 3890.844    0.001 3890.844    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                2538667 2063.293    0.001 3651.151    0.001 replaybuffer.py:28(teleporter_save_data)
                2538667 1815.393    0.001 3470.806    0.001 agent.py:88(interveen)
               84735223  178.934    0.000 3312.375    0.000 linear.py:93(forward)
               84735223   68.886    0.000 3038.124    0.000 functional.py:1737(linear)
               84735223 2952.952    0.000 2952.952    0.000 {built-in method torch._C._nn.linear}
              253652862  542.591    0.000 2741.626    0.000 layers.py:838(isFree)
             2452530470 1782.466    0.000 2199.035    0.000 layer.py:103(isFree)
                2538667 1316.027    0.001 1962.783    0.001 agent.py:67(modify)
                4601118   57.035    0.000 1827.605    0.000 layers.py:849(restart)
               13695607   92.766    0.000 1784.443    0.000 agent.py:59(modify_board)
              114672742  102.644    0.000 1779.601    0.000 activation.py:713(forward)
                6087244 1495.938    0.000 1726.776    0.000 agent.py:187(convert_values)
              114672742   94.513    0.000 1676.957    0.000 functional.py:1364(leaky_relu)
              159291339 1608.230    0.000 1608.230    0.000 {built-in method clone}
              114672742 1562.910    0.000 1562.910    0.000 {built-in method torch._C._nn.leaky_relu}
             5394935079 1034.613    0.000 1487.953    0.000 enum.py:646(__hash__)
             1289768301 1439.766    0.000 1439.766    0.000 layer.py:154(elements)
               39082277 1433.534    0.000 1433.534    0.000 {built-in method cat}
                2538667 1003.199    0.000 1326.650    0.001 replaybuffer.py:73(CF_save_data)
                4601118   24.903    0.000 1313.060    0.000 level.py:8(__init__)
              256881582  277.209    0.000 1216.198    0.000 {built-in method builtins.any}
                2538667   43.279    0.000 1168.230    0.000 agent.py:172(__call__)
               13695607 1162.333    0.000 1162.333    0.000 {built-in method torch._C._nn.one_hot}
                2538667   40.578    0.000 1079.916    0.000 agent.py:112(__call__)
                4601118  161.051    0.000 1058.041    0.000 levels.py:199(generate)
              142165352 1022.643    0.000 1022.643    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              253652862  758.756    0.000 1020.891    0.000 layers.py:77(check)
              253652862  601.861    0.000  970.582    0.000 layers.py:286(check)
             2741921402  774.771    0.000  938.989    0.000 layers.py:809(<genexpr>)
              142165352  908.651    0.000  908.651    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                7616001  160.849    0.000  898.933    0.000 optimizer.py:189(zero_grad)
              253866700  102.339    0.000  879.205    0.000 {built-in method builtins.all}
              253652862  511.799    0.000  878.842    0.000 layers.py:246(check)
            12159265736  786.526    0.000  861.295    0.000 {built-in method builtins.len}
             1041128491  289.435    0.000  810.068    0.000 layers.py:799(<genexpr>)
                9202236   82.552    0.000  741.053    0.000 level.py:41(notUsed)
               11156940  272.039    0.000  720.086    0.000 exploration.py:53(softmaxer)
             6587392424  700.565    0.000  700.565    0.000 layer.py:99(positions)
               71082676  592.976    0.000  592.976    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                2538667   44.394    0.000  591.009    0.000 replaybuffer.py:18(stacker)
                2538667   46.250    0.000  575.488    0.000 replaybuffer.py:63(stacker)
              253652862  383.970    0.000  538.977    0.000 layers.py:62(check)
               71082676  512.685    0.000  512.685    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               71082676  484.790    0.000  484.790    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               71082676  480.312    0.000  480.312    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              253866700  315.090    0.000  478.522    0.000 layers.py:113(isDone)
             5394964230  453.345    0.000  453.345    0.000 {built-in method builtins.hash}
              253652862  275.191    0.000  444.193    0.000 layers.py:313(check)
               14279570  170.017    0.000  443.464    0.000 random.py:315(sample)
               46011180   65.116    0.000  440.913    0.000 layer.py:77(restart)
              253652862  276.462    0.000  437.924    0.000 layers.py:273(check)
              497578732  338.749    0.000  421.833    0.000 tensor.py:906(grad)
                2538667  236.248    0.000  402.013    0.000 collector.py:46(collect)
              101546660  397.533    0.000  397.533    0.000 layer.py:171(<listcomp>)
              293074404  306.829    0.000  397.050    0.000 layer.py:134(remove)
              253652862  238.044    0.000  362.704    0.000 layers.py:48(check)
              175525613  360.457    0.000  360.457    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               71082676  356.786    0.000  356.786    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                7616001   11.650    0.000  334.768    0.000 loss.py:527(forward)
              101546660  326.377    0.000  326.377    0.000 layer.py:172(<listcomp>)
                7616001   30.099    0.000  323.118    0.000 functional.py:2898(mse_loss)
               27727473  320.455    0.000  320.455    0.000 {method 'item' of 'torch._C._TensorBase' objects}
              545399148  225.814    0.000  310.585    0.000 layer.py:138(add)
                9202236    9.745    0.000  305.664    0.000 level.py:38(elementsIn)
              253652862  202.313    0.000  298.519    0.000 layers.py:23(check)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9621662: <Causal4_Conver4_3counterfacts_2_2> in cluster <dcc> Done

Job <Causal4_Conver4_3counterfacts_2_2> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Fri May  7 14:30:14 2021
Job was executed on host(s) <n-62-20-15>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Fri May  7 14:51:36 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Fri May  7 14:51:36 2021
Terminated at Sat May  8 14:47:03 2021
Results reported at Sat May  8 14:47:03 2021

Your job looked like:

------------------------------------------------------------
# LSBATCH: User input
#!/bin/sh
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

python main.py $MYARGS


------------------------------------------------------------

Successfully completed.

Resource usage summary:

    CPU time :                                   85893.88 sec.
    Max Memory :                                 8200 MB
    Average Memory :                             5726.66 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               8184.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86126 sec.
    Turnaround time :                            87409 sec.

The output (if any) is above this job summary.

