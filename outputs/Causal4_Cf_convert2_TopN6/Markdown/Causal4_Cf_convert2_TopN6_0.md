
# Parameters

    Name :                      Causal4_Cf_convert2_TopN6-0
    Main :                      CFagent
    Level :                     Levels.Causal4
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
    Topn :                      6
    Random counterfacts :       False
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      65675599414 function calls (65380671307 primitive calls) in 86117.63 seconds

##    Ordered by: cumulative time
   List reduced from 515 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86117.625 86117.625 {built-in method builtins.exec}
                      1    4.691    4.691 86117.625 86117.625 <string>:1(<module>)
                      1  420.364  420.364 86112.935 86112.935 main.py:79(CFagent)
                9505779   44.042    0.000 25196.731    0.003 agent.py:29(learn)
                3168593   18.813    0.000 20890.657    0.007 game.py:41(step)
                9505777  648.890    0.000 20292.351    0.002 learner.py:42(Qlearn)
                3168593   22.882    0.000 20078.852    0.006 layers.py:718(step)
                3168593  316.544    0.000 13374.464    0.004 layers.py:17(step)
              315898876  955.768    0.000 13029.401    0.000 layer.py:98(move)
        330065592/35139176 1468.896    0.000 11578.207    0.000 module.py:866(_call_impl)
               25633399   86.152    0.000 10770.940    0.000 network.py:27(forward)
               25633399  372.829    0.000 10484.015    0.000 container.py:117(forward)
                3168593  910.371    0.000 10457.690    0.003 agent.py:210(counterfact)
                3168593  390.708    0.000 9826.826    0.003 agent.py:54(_learn)
                3168593  382.861    0.000 8922.451    0.003 agent.py:202(_learn)
              315898876 1468.261    0.000 7942.726    0.000 layers.py:735(check)
                3168593 6819.705    0.002 7925.212    0.003 replaybuffer.py:22(sample_data)
                9505777  107.558    0.000 7837.194    0.001 optimizer.py:84(wrapper)
                3168593 6375.261    0.002 7422.565    0.002 replaybuffer.py:67(sample_data)
                9505777   56.971    0.000 7414.346    0.001 grad_mode.py:24(decorate_context)
                9505777  334.727    0.000 7233.907    0.001 adam.py:55(step)
                3168594  482.754    0.000 6646.995    0.002 layers.py:684(update)
                9505777 1500.680    0.000 6535.765    0.001 _functional.py:53(adam)
                3168593  105.089    0.000 6376.792    0.002 agent.py:117(_learn)
                8060422  265.016    0.000 5725.302    0.001 agent.py:49(__call__)
               50317751 5437.876    0.000 5437.876    0.000 {built-in method tensor}
                9505777   46.811    0.000 5338.512    0.001 tensor.py:195(backward)
                9505777   51.316    0.000 5290.203    0.001 __init__.py:68(backward)
               43009634   30.641    0.000 5244.455    0.000 game.py:37(board)
                9505777 5024.317    0.001 5024.317    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
               63371870 2909.721    0.000 4963.621    0.000 layer.py:151(update)
                3168593 1823.433    0.001 4009.721    0.001 agent.py:88(interveen)
               51266798  125.181    0.000 3882.445    0.000 conv.py:398(forward)
               51266798   86.240    0.000 3695.588    0.000 conv.py:390(_conv_forward)
               51266798 3609.348    0.000 3609.348    0.000 {built-in method conv2d}
                3168593 2052.172    0.001 3533.096    0.001 replaybuffer.py:28(teleporter_save_data)
              315898876  585.057    0.000 3464.227    0.000 layers.py:729(isFree)
               70563011  146.420    0.000 2921.005    0.000 linear.py:93(forward)
             2759680679 2418.580    0.000 2879.171    0.000 layer.py:95(isFree)
               70563011   61.008    0.000 2691.272    0.000 functional.py:1737(linear)
               70563011 2615.389    0.000 2615.389    0.000 {built-in method torch._C._nn.linear}
                3168593 1659.090    0.001 2537.146    0.001 agent.py:67(modify)
                1730016   40.472    0.000 2487.385    0.001 agent.py:175(choose_action)
               42914935 1751.040    0.000 1751.040    0.000 {built-in method cat}
               11229015   92.177    0.000 1616.100    0.000 agent.py:59(modify_board)
             5969019381 1139.581    0.000 1613.417    0.000 enum.py:646(__hash__)
                3168591   68.868    0.000 1575.002    0.000 agent.py:171(__call__)
               96196410   87.777    0.000 1545.304    0.000 activation.py:713(forward)
              316771490  330.286    0.000 1485.973    0.000 {built-in method builtins.any}
              139743871 1472.912    0.000 1472.912    0.000 {built-in method clone}
               96196410   87.206    0.000 1457.527    0.000 functional.py:1364(leaky_relu)
                3168593   63.688    0.000 1411.569    0.000 agent.py:112(__call__)
               96196410 1353.629    0.000 1353.629    0.000 {built-in method torch._C._nn.leaky_relu}
              177441168 1281.382    0.000 1281.382    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                3256504   44.528    0.000 1275.992    0.000 layers.py:740(restart)
              315898876  964.932    0.000 1270.439    0.000 layers.py:77(check)
             1082903889 1255.145    0.000 1255.145    0.000 layer.py:146(elements)
                3168593  969.393    0.000 1225.180    0.000 replaybuffer.py:73(CF_save_data)
              315898876  789.563    0.000 1192.627    0.000 layers.py:246(check)
             3449631856  958.684    0.000 1155.687    0.000 layers.py:700(<genexpr>)
                9505777  200.728    0.000 1144.113    0.000 optimizer.py:189(zero_grad)
              177441168 1118.978    0.000 1118.978    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               11229015 1064.964    0.000 1064.964    0.000 {built-in method torch._C._nn.one_hot}
              315898876  632.708    0.000 1042.168    0.000 layers.py:286(check)
                3256504   21.855    0.000  898.686    0.000 level.py:8(__init__)
                3168593   75.143    0.000  836.474    0.000 replaybuffer.py:18(stacker)
                3168591   70.542    0.000  789.409    0.000 replaybuffer.py:63(stacker)
              315898876  597.949    0.000  762.923    0.000 layers.py:62(check)
               88720584  738.628    0.000  738.628    0.000 {method 'add' of 'torch._C._TensorBase' objects}
             7685342730  721.453    0.000  721.453    0.000 layer.py:91(positions)
                3256504  114.683    0.000  708.580    0.000 levels.py:199(generate)
              316859400  107.137    0.000  659.072    0.000 {built-in method builtins.all}
               88720584  654.236    0.000  654.236    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
        8387001787/8387001784  563.918    0.000  631.428    0.000 {built-in method builtins.len}
               88720584  608.415    0.000  608.415    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               88720584  604.694    0.000  604.694    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
                8060422  207.876    0.000  591.909    0.000 exploration.py:53(softmaxer)
             1137699764  297.394    0.000  590.901    0.000 layers.py:690(<genexpr>)
               12850194  222.234    0.000  571.799    0.000 random.py:315(sample)
              621044172  459.300    0.000  567.153    0.000 tensor.py:906(grad)
              315898876  344.186    0.000  544.071    0.000 layers.py:313(check)
              315898876  337.369    0.000  532.923    0.000 layers.py:273(check)
                3168593  292.414    0.000  503.229    0.000 collector.py:46(collect)
                9505777   19.589    0.000  484.587    0.000 loss.py:527(forward)
                6513008   57.262    0.000  479.072    0.000 level.py:41(notUsed)
             5969055476  473.843    0.000  473.843    0.000 {built-in method builtins.hash}
                1730016  413.952    0.000  466.929    0.000 agent.py:186(convert_values)
                9505777   51.006    0.000  464.997    0.000 functional.py:2898(mse_loss)
              315898876  313.872    0.000  456.623    0.000 layers.py:48(check)
               88720584  444.626    0.000  444.626    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              315898876  245.120    0.000  355.609    0.000 layers.py:23(check)
              154141477  325.943    0.000  325.943    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               32565040   47.196    0.000  321.376    0.000 layer.py:69(restart)
              287242509  209.434    0.000  299.963    0.000 layer.py:126(remove)
              479027093  212.785    0.000  298.860    0.000 layer.py:130(add)
             3488786165  287.659    0.000  287.659    0.000 {method 'random' of '_random.Random' objects}
                6337188  279.546    0.000  279.546    0.000 {built-in method nonzero}
                9505777  274.783    0.000  274.783    0.000 {built-in method torch._C._nn.mse_loss}
               63371870  274.710    0.000  274.710    0.000 layer.py:163(<listcomp>)
              384533137  182.138    0.000  270.844    0.000 random.py:250(_randbelow_with_getrandbits)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9533958: <Causal4_Cf_convert2_TopN6_0> in cluster <dcc> Done

Job <Causal4_Cf_convert2_TopN6_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Sun Apr 18 20:20:07 2021
Job was executed on host(s) <n-62-20-10>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sun Apr 18 20:20:08 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sun Apr 18 20:20:08 2021
Terminated at Mon Apr 19 20:15:41 2021
Results reported at Mon Apr 19 20:15:41 2021

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

    CPU time :                                   85859.48 sec.
    Max Memory :                                 9460 MB
    Average Memory :                             6431.02 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               6924.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86239 sec.
    Turnaround time :                            86134 sec.

The output (if any) is above this job summary.

