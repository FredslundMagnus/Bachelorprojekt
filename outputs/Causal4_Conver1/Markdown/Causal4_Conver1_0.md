
# Parameters

    Name :                      Causal4_Conver1-0
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
    Cf convert :                1
    Counterfacts :              1
    Topn :                      3
    Random counterfacts :       False
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      62320198483 function calls (62037895356 primitive calls) in 86124.30 seconds

##    Ordered by: cumulative time
   List reduced from 514 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86124.296 86124.296 {built-in method builtins.exec}
                      1    4.710    4.710 86124.296 86124.296 <string>:1(<module>)
                      1  442.774  442.774 86119.585 86119.585 main.py:79(CFagent)
                9102702   54.488    0.000 25874.108    0.003 agent.py:29(learn)
                9102700  690.387    0.000 20620.416    0.002 learner.py:42(Qlearn)
                3034234   20.689    0.000 20495.416    0.007 game.py:41(step)
                3034234   22.300    0.000 19609.277    0.006 layers.py:718(step)
                3034234  311.597    0.000 13079.501    0.004 layers.py:17(step)
              303098571  937.639    0.000 12740.776    0.000 layer.py:98(move)
        315940667/33639231 1479.777    0.000 11965.331    0.000 module.py:866(_call_impl)
               24536531   85.230    0.000 11073.414    0.000 network.py:27(forward)
               24536531  367.577    0.000 10790.588    0.000 container.py:117(forward)
                3034234  903.378    0.000 10283.110    0.003 agent.py:212(counterfact)
                3034234  419.699    0.000 10079.777    0.003 agent.py:54(_learn)
                3034234  415.720    0.000 9062.532    0.003 agent.py:204(_learn)
                3034234 6808.961    0.002 7933.177    0.003 replaybuffer.py:22(sample_data)
              303098571 1447.360    0.000 7813.232    0.000 layers.py:735(check)
                9102700  114.166    0.000 7693.606    0.001 optimizer.py:84(wrapper)
                3034234 6358.863    0.002 7425.332    0.002 replaybuffer.py:67(sample_data)
                9102700   61.190    0.000 7211.129    0.001 grad_mode.py:24(decorate_context)
                9102700  346.028    0.000 7014.154    0.001 adam.py:55(step)
                3034234  118.262    0.000 6651.054    0.002 agent.py:117(_learn)
                3034235  498.245    0.000 6470.216    0.002 layers.py:684(update)
                9102700 1457.185    0.000 6314.359    0.001 _functional.py:53(adam)
                7713044  284.152    0.000 6072.234    0.001 agent.py:49(__call__)
                9102700   54.754    0.000 5606.925    0.001 tensor.py:195(backward)
                9102700   54.053    0.000 5550.688    0.001 __init__.py:68(backward)
               48199098 5419.374    0.000 5419.374    0.000 {built-in method tensor}
                9102700 5247.417    0.001 5247.417    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
               41187047   33.636    0.000 5221.844    0.000 game.py:37(board)
               60684690 2930.038    0.000 4994.521    0.000 layer.py:151(update)
               49073062  131.543    0.000 4179.413    0.000 conv.py:398(forward)
                3034234 1694.856    0.001 4005.268    0.001 agent.py:88(interveen)
               49073062   98.097    0.000 3981.820    0.000 conv.py:390(_conv_forward)
               49073062 3883.723    0.000 3883.723    0.000 {built-in method conv2d}
              303098571  577.657    0.000 3332.779    0.000 layers.py:729(isFree)
                3034234 1864.070    0.001 3219.258    0.001 replaybuffer.py:28(teleporter_save_data)
               67541125  147.334    0.000 3014.337    0.000 linear.py:93(forward)
               67541125   63.647    0.000 2786.624    0.000 functional.py:1737(linear)
             2573066050 2326.621    0.000 2755.122    0.000 layer.py:95(isFree)
               67541125 2709.290    0.000 2709.290    0.000 {built-in method torch._C._nn.linear}
                3034234 1707.778    0.001 2697.651    0.001 agent.py:67(modify)
                1652321   40.775    0.000 2415.895    0.001 agent.py:176(choose_action)
               10747278   98.206    0.000 1782.262    0.000 agent.py:59(modify_board)
               41089608 1767.961    0.000 1767.961    0.000 {built-in method cat}
                3034232   70.459    0.000 1657.072    0.001 agent.py:172(__call__)
             5724253977 1086.395    0.000 1555.430    0.000 enum.py:646(__hash__)
               92077656   95.425    0.000 1519.618    0.000 activation.py:713(forward)
                3034234   67.574    0.000 1435.867    0.000 agent.py:112(__call__)
               92077656   92.730    0.000 1424.193    0.000 functional.py:1364(leaky_relu)
              303333816  320.473    0.000 1390.646    0.000 {built-in method builtins.any}
              129002043 1368.085    0.000 1368.085    0.000 {built-in method clone}
               92077656 1315.252    0.000 1315.252    0.000 {built-in method torch._C._nn.leaky_relu}
             1028643613 1286.483    0.000 1286.483    0.000 layer.py:146(elements)
              303098571  977.276    0.000 1269.398    0.000 layers.py:77(check)
                3123919   46.816    0.000 1248.857    0.000 layers.py:740(restart)
                3034234  964.066    0.000 1217.677    0.000 replaybuffer.py:73(CF_save_data)
              169917064 1216.719    0.000 1216.719    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               10747278 1179.539    0.000 1179.539    0.000 {built-in method torch._C._nn.one_hot}
              303098571  762.037    0.000 1149.372    0.000 layers.py:286(check)
                9102700  206.076    0.000 1106.447    0.000 optimizer.py:189(zero_grad)
             3303295391  876.824    0.000 1070.172    0.000 layers.py:700(<genexpr>)
              169917064 1060.746    0.000 1060.746    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              303098571  630.534    0.000 1029.288    0.000 layers.py:246(check)
                3123919   20.778    0.000  874.959    0.000 level.py:8(__init__)
                3034234   75.899    0.000  838.823    0.000 replaybuffer.py:18(stacker)
                3034232   77.840    0.000  793.610    0.000 replaybuffer.py:63(stacker)
              303098571  592.327    0.000  749.287    0.000 layers.py:62(check)
               84958532  720.020    0.000  720.020    0.000 {method 'add' of 'torch._C._TensorBase' objects}
             7351693980  712.426    0.000  712.426    0.000 layer.py:91(positions)
                3123919  111.542    0.000  685.799    0.000 levels.py:199(generate)
                7713044  233.263    0.000  662.298    0.000 exploration.py:53(softmaxer)
               84958532  639.096    0.000  639.096    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
        8055873642/8055873639  542.767    0.000  613.843    0.000 {built-in method builtins.len}
               12316306  232.892    0.000  602.784    0.000 random.py:315(sample)
               84958532  598.770    0.000  598.770    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               84958532  592.429    0.000  592.429    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              303423500   82.953    0.000  538.209    0.000 {built-in method builtins.all}
              303098571  335.267    0.000  535.748    0.000 layers.py:313(check)
                9102700   23.795    0.000  530.103    0.000 loss.py:527(forward)
              594709808  423.775    0.000  525.002    0.000 tensor.py:906(grad)
              303098571  323.130    0.000  515.445    0.000 layers.py:273(check)
                9102700   56.741    0.000  506.308    0.000 functional.py:2898(mse_loss)
              881534748  228.172    0.000  493.874    0.000 layers.py:690(<genexpr>)
                3034234  284.594    0.000  490.397    0.000 collector.py:46(collect)
             5724288616  469.041    0.000  469.041    0.000 {built-in method builtins.hash}
              303098571  319.877    0.000  462.782    0.000 layers.py:48(check)
                6247838   56.650    0.000  461.437    0.000 level.py:41(notUsed)
               84958532  425.973    0.000  425.973    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                1652321  359.022    0.000  359.022    0.000 agent.py:187(convert_values)
              303098571  232.440    0.000  341.873    0.000 layers.py:23(check)
               31239190   45.544    0.000  316.351    0.000 layer.py:69(restart)
              270102244  225.127    0.000  311.245    0.000 layer.py:126(remove)
              142783553  300.825    0.000  300.825    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
                6068470  297.877    0.000  297.877    0.000 {built-in method nonzero}
                9102700  295.806    0.000  295.806    0.000 {built-in method torch._C._nn.mse_loss}
              454510453  212.074    0.000  288.341    0.000 layer.py:130(add)
             3346815101  282.677    0.000  282.677    0.000 {method 'random' of '_random.Random' objects}
               60684690  279.715    0.000  279.715    0.000 layer.py:163(<listcomp>)
              365514062  182.390    0.000  274.848    0.000 random.py:250(_randbelow_with_getrandbits)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9579160: <Causal4_Conver1_0> in cluster <dcc> Done

Job <Causal4_Conver1_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Tue Apr 27 02:44:06 2021
Job was executed on host(s) <n-62-20-12>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Wed Apr 28 08:24:25 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Wed Apr 28 08:24:25 2021
Terminated at Thu Apr 29 08:20:05 2021
Results reported at Thu Apr 29 08:20:05 2021

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

    CPU time :                                   85893.59 sec.
    Max Memory :                                 8974 MB
    Average Memory :                             6085.66 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               7410.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86141 sec.
    Turnaround time :                            192959 sec.

The output (if any) is above this job summary.

