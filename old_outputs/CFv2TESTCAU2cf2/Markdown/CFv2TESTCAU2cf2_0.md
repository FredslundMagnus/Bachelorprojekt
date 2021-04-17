
# Parameters

    Name :                      CFv2TESTCAU2cf2-0
    Main :                      CFagentv2
    Level :                     Levels.Causal2
    Failed actions chance :     0.0
    Hours :                     16.0
    Batch :                     100
    Width :                     9
    Height :                    9
    Network1 :                  Networks.Teleporter
    K1 :                        500000
    Learner1 :                  Learners.Qlearn
    Exploration1 :              Explorations.softmaxer
    Gamma1 :                    0.98
    Network2 :                  Networks.Mini
    K2 :                        100000
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
    Reset chance :              0.001
    Modified done chance :      0.05
    Miss intervention cost :    -0.15
    Intervention cost :         -0.05
    Replay size :               100000
    Sample size :               50
    Cf convert :                3
    Counterfacts :              2
    Topn :                      5
    Minutes used :              955 minutes.
    Hours used :                15 hours.

# Profiling


      35225709486 function calls (35057887700 primitive calls) in 57315.17 seconds

##    Ordered by: cumulative time
   List reduced from 516 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 57315.174 57315.174 {built-in method builtins.exec}
                      1    5.876    5.876 57315.174 57315.174 <string>:1(<module>)
                      1  171.115  171.115 57309.299 57309.299 main.py:103(CFagentv2)
                5790333   22.155    0.000 17483.640    0.003 agent.py:29(learn)
                5787945  441.535    0.000 14541.715    0.003 learner.py:42(Qlearn)
                1930111   10.298    0.000 8672.323    0.004 game.py:41(step)
                1930111   12.805    0.000 8235.887    0.004 layers.py:719(step)
                7718056   66.957    0.000 7507.658    0.001 optimizer.py:84(wrapper)
        191169282/23349208  819.012    0.000 7376.913    0.000 module.py:866(_call_impl)
                7718056   32.911    0.000 7192.800    0.001 grad_mode.py:24(decorate_context)
                7718056  225.585    0.000 7082.723    0.001 adam.py:55(step)
                1930111  203.258    0.000 6741.484    0.003 agent.py:54(_learn)
               15631152  221.709    0.000 6660.748    0.000 container.py:117(forward)
                7718056 1455.426    0.000 6624.198    0.001 _functional.py:53(adam)
                1930111  199.123    0.000 6265.454    0.003 agent.py:202(_learn)
               13625601   38.163    0.000 6162.319    0.000 network.py:24(forward)
                1930111 1555.603    0.001 5602.984    0.003 agent.py:236(counterfact2)
                7718056   31.902    0.000 4548.446    0.001 tensor.py:195(backward)
                7718056   29.791    0.000 4515.389    0.001 __init__.py:68(backward)
                1930111  168.911    0.000 4505.433    0.002 layers.py:17(step)
                1930111   58.243    0.000 4442.024    0.002 agent.py:117(_learn)
              191540679  301.920    0.000 4320.307    0.000 layer.py:98(move)
                7718056 4313.871    0.001 4313.871    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                1930111 3443.488    0.002 3926.311    0.002 replaybuffer.py:85(sample_data)
                1930111   33.853    0.000 3904.711    0.002 simulator.py:50(learn)
                1930111  215.700    0.000 3870.858    0.002 simulator.py:23(learn)
                1930112  283.780    0.000 3698.969    0.002 layers.py:685(update)
                1930111 2815.638    0.001 3450.352    0.002 replaybuffer.py:22(sample_data)
                1930111 2632.153    0.001 3247.396    0.002 replaybuffer.py:52(sample_data)
                3904382  106.030    0.000 2883.799    0.001 agent.py:49(__call__)
              191540679  560.645    0.000 2685.890    0.000 layers.py:736(check)
               33267855   74.567    0.000 2608.121    0.000 conv.py:398(forward)
               29279934 2498.811    0.000 2498.811    0.000 {built-in method tensor}
               33267855   46.475    0.000 2496.501    0.000 conv.py:390(_conv_forward)
               33267855 2450.026    0.000 2450.026    0.000 {built-in method conv2d}
               24990439   16.573    0.000 2374.395    0.000 game.py:37(board)
                1930111  948.813    0.000 2345.800    0.001 agent.py:88(interveen)
                1930111 1475.925    0.001 2081.294    0.001 replaybuffer.py:58(CF_save_data)
                1930111  961.191    0.000 1809.588    0.001 replaybuffer.py:28(teleporter_save_data)
               27021561 1063.594    0.000 1801.630    0.000 layer.py:167(NoRock_update)
                1930111 1176.163    0.001 1743.379    0.001 agent.py:67(modify)
               37016581   77.338    0.000 1740.849    0.000 linear.py:93(forward)
               37016581   31.145    0.000 1623.097    0.000 functional.py:1737(linear)
               37016581 1584.504    0.000 1584.504    0.000 {built-in method torch._C._nn.linear}
                3800433   35.784    0.000 1425.697    0.000 layers.py:741(restart)
               32919547 1415.073    0.000 1415.073    0.000 {built-in method cat}
              131199788 1353.944    0.000 1353.944    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              102721479 1349.283    0.000 1349.283    0.000 {built-in method clone}
              131199788 1184.664    0.000 1184.664    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                3800433   17.819    0.000 1136.220    0.000 level.py:8(__init__)
                1930111  885.132    0.000 1095.080    0.001 replaybuffer.py:91(simulator_save_data)
              191540679  222.020    0.000 1094.302    0.000 layers.py:730(isFree)
               54653284   46.780    0.000 1049.854    0.000 activation.py:713(forward)
                7718056  171.591    0.000 1048.511    0.000 optimizer.py:189(zero_grad)
               54653284   49.648    0.000 1003.074    0.000 functional.py:1364(leaky_relu)
                1927723   37.538    0.000 1001.929    0.001 agent.py:171(__call__)
                3800433   44.179    0.000  973.244    0.000 levels.py:151(generate)
               54653284  943.639    0.000  943.639    0.000 {built-in method torch._C._nn.leaky_relu}
                1930111   37.513    0.000  928.862    0.000 agent.py:112(__call__)
               18244095  159.938    0.000  886.394    0.000 level.py:41(notUsed)
              991511803  749.126    0.000  872.283    0.000 layer.py:95(isFree)
                5834493   41.596    0.000  856.325    0.000 agent.py:59(modify_board)
             3239484213  531.131    0.000  762.467    0.000 enum.py:646(__hash__)
                7840044  748.467    0.000  748.467    0.000 {built-in method torch._C._nn.one_hot}
               65599894  745.984    0.000  745.984    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                2005551    8.785    0.000  658.720    0.000 simulator.py:20(boardforward)
               65599894  651.744    0.000  651.744    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               65599894  608.606    0.000  608.606    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               65599894  604.704    0.000  604.704    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              191140879  146.397    0.000  594.153    0.000 {built-in method builtins.any}
              191540679  342.021    0.000  527.709    0.000 layers.py:232(check)
              191540679  330.631    0.000  522.796    0.000 layers.py:208(check)
               40166762  513.904    0.000  513.904    0.000 {method 'item' of 'torch._C._TensorBase' objects}
                1930111   34.276    0.000  496.931    0.000 replaybuffer.py:18(stacker)
              191540679  305.534    0.000  483.858    0.000 layers.py:220(check)
                1927723   34.564    0.000  483.681    0.000 replaybuffer.py:48(stacker)
               65599894  471.559    0.000  471.559    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
             1513686136  363.323    0.000  447.756    0.000 layers.py:701(<genexpr>)
              193011200   37.035    0.000  446.475    0.000 {built-in method builtins.all}
              408463456   88.762    0.000  432.822    0.000 layers.py:691(<genexpr>)
              583761225  432.035    0.000  432.035    0.000 layer.py:146(elements)
               11404224  429.627    0.000  429.627    0.000 {built-in method nonzero}
               18244095   13.525    0.000  416.670    0.000 level.py:38(elementsIn)
                5790333  150.715    0.000  392.136    0.000 random.py:315(sample)
                1930111  242.071    0.000  391.187    0.000 collector.py:46(collect)
                7718056   11.174    0.000  389.729    0.000 loss.py:527(forward)
              459199348  307.900    0.000  380.248    0.000 tensor.py:906(grad)
                7718056   32.807    0.000  378.555    0.000 functional.py:2898(mse_loss)
                1930111   27.550    0.000  348.718    0.000 replaybuffer.py:81(stacker)
              112489246  347.997    0.000  347.997    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              193011200  233.087    0.000  339.862    0.000 layers.py:114(isDone)
             3581515967  320.530    0.000  320.530    0.000 layer.py:91(positions)
                3904382  111.725    0.000  314.001    0.000 exploration.py:53(softmaxer)
        3990365613/3990365609  273.786    0.000  312.135    0.000 {built-in method builtins.len}
                1930111   52.276    0.000  268.142    0.000 agent.py:277(counterfact_check)
               18244095  134.206    0.000  267.288    0.000 level.py:39(<listcomp>)
              191540679  177.856    0.000  261.316    0.000 layers.py:197(check)
                7718056  250.582    0.000  250.582    0.000 {built-in method torch._C._nn.mse_loss}
               26603031   22.988    0.000  244.492    0.000 layer.py:69(restart)
              265622821  203.560    0.000  244.325    0.000 layer.py:130(add)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-3>
Subject: Job 9511602: <CFv2TESTCAU2cf2_0> in cluster <dcc> Done

Job <CFv2TESTCAU2cf2_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Mon Apr 12 20:13:41 2021
Job was executed on host(s) <n-62-20-3>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Mon Apr 12 20:23:39 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Mon Apr 12 20:23:39 2021
Terminated at Tue Apr 13 12:19:01 2021
Results reported at Tue Apr 13 12:19:01 2021

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

    CPU time :                                   57170.61 sec.
    Max Memory :                                 8588 MB
    Average Memory :                             6199.04 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               7796.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   57323 sec.
    Turnaround time :                            57920 sec.

The output (if any) is above this job summary.

