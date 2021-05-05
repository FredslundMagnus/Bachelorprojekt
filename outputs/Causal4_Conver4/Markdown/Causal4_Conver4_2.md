
# Parameters

    Name :                      Causal4_Conver4-2
    Main :                      CFagent
    Level :                     Levels.Causal4
    Failed actions chance :     0
    Use model :                 True
    Depth :                     3
    Model explore :             1000000
    Samples :                   5
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
    Counterfacts :              1
    Topn :                      3
    Random counterfacts :       False
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      78842217719 function calls (78499559316 primitive calls) in 86109.57 seconds

##    Ordered by: cumulative time
   List reduced from 514 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86109.569 86109.569 {built-in method builtins.exec}
                      1    4.378    4.378 86109.569 86109.569 <string>:1(<module>)
                      1  400.171  400.171 86105.191 86105.191 main.py:80(CFagent)
               11050209   41.740    0.000 25771.288    0.002 agent.py:29(learn)
                3683403   16.697    0.000 22090.670    0.006 game.py:42(step)
                3683403   20.245    0.000 21253.503    0.006 layers.py:827(step)
               11050209  646.389    0.000 20913.604    0.002 learner.py:42(Qlearn)
                3683403  311.503    0.000 14093.860    0.004 layers.py:17(step)
              368082052  986.578    0.000 13749.506    0.000 layer.py:106(move)
        383489448/40832736 1481.002    0.000 12015.919    0.000 module.py:866(_call_impl)
               29782527   78.678    0.000 11240.333    0.000 network.py:28(forward)
               29782527  355.858    0.000 10978.982    0.000 container.py:117(forward)
                3683403  895.247    0.000 10784.673    0.003 agent.py:212(counterfact)
                3683403  383.949    0.000 10015.001    0.003 agent.py:54(_learn)
                3683403  378.612    0.000 9204.447    0.002 agent.py:204(_learn)
              368082052 1696.952    0.000 8457.570    0.000 layers.py:844(check)
               11050209   88.365    0.000 8123.335    0.001 optimizer.py:84(wrapper)
               11050209   46.188    0.000 7713.535    0.001 grad_mode.py:24(decorate_context)
               11050209  315.158    0.000 7570.085    0.001 adam.py:55(step)
                3683404  514.532    0.000 7109.132    0.002 layers.py:793(update)
               11050209 1578.114    0.000 6896.138    0.001 _functional.py:53(adam)
                3683403  111.843    0.000 6486.854    0.002 agent.py:117(_learn)
                3683403 5349.228    0.001 6469.888    0.002 replaybuffer.py:22(sample_data)
                3683403 5333.954    0.001 6415.953    0.002 replaybuffer.py:67(sample_data)
               58339145 5906.285    0.000 5906.285    0.000 {built-in method tensor}
                9361720  238.221    0.000 5777.440    0.001 agent.py:49(__call__)
               49895559   30.090    0.000 5709.468    0.000 game.py:38(board)
               11050209   42.539    0.000 5404.863    0.000 tensor.py:195(backward)
               11050209   39.980    0.000 5360.988    0.000 __init__.py:68(backward)
               11050209 5112.187    0.000 5112.187    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
               73668070 2657.094    0.000 4561.009    0.000 layer.py:159(update)
                3683403 1831.804    0.000 4093.329    0.001 agent.py:88(interveen)
               59565054  126.841    0.000 4084.152    0.000 conv.py:398(forward)
               59565054   81.442    0.000 3898.801    0.000 conv.py:390(_conv_forward)
               59565054 3817.359    0.000 3817.359    0.000 {built-in method conv2d}
                3683403 2072.492    0.001 3648.702    0.001 replaybuffer.py:28(teleporter_save_data)
              368082052  716.931    0.000 3611.845    0.000 layers.py:838(isFree)
               81980775  163.758    0.000 3101.004    0.000 linear.py:93(forward)
             3482810185 2369.226    0.000 2894.914    0.000 layer.py:103(isFree)
               81980775   65.349    0.000 2860.265    0.000 functional.py:1737(linear)
               81980775 2779.418    0.000 2779.418    0.000 {built-in method torch._C._nn.linear}
                2003792   39.996    0.000 2633.870    0.001 agent.py:176(choose_action)
                3683403 1690.330    0.000 2565.829    0.001 agent.py:67(modify)
               49879153 1835.184    0.000 1835.184    0.000 {built-in method cat}
             7025769397 1201.967    0.000 1741.586    0.000 enum.py:646(__hash__)
              111763302   87.785    0.000 1641.125    0.000 activation.py:713(forward)
              368332872  359.558    0.000 1628.212    0.000 {built-in method builtins.any}
               13045123   77.234    0.000 1622.119    0.000 agent.py:59(modify_board)
                3683403   61.705    0.000 1590.457    0.000 agent.py:172(__call__)
              111763302   84.957    0.000 1553.340    0.000 functional.py:1364(leaky_relu)
              164112591 1543.757    0.000 1543.757    0.000 {built-in method clone}
                3683403   57.984    0.000 1500.780    0.000 agent.py:112(__call__)
              111763302 1450.672    0.000 1450.672    0.000 {built-in method torch._C._nn.leaky_relu}
                3690932   46.020    0.000 1359.197    0.000 layers.py:849(restart)
              206270568 1346.431    0.000 1346.431    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              368082052 1003.146    0.000 1325.175    0.000 layers.py:77(check)
             4011144148 1054.334    0.000 1268.654    0.000 layers.py:809(<genexpr>)
              368082052  797.043    0.000 1242.239    0.000 layers.py:286(check)
               11050209  214.965    0.000 1231.509    0.000 optimizer.py:189(zero_grad)
                3683403  964.861    0.000 1221.445    0.000 replaybuffer.py:73(CF_save_data)
              206270568 1193.580    0.000 1193.580    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              368082052  667.286    0.000 1107.124    0.000 layers.py:246(check)
             1250044989 1074.954    0.000 1074.954    0.000 layer.py:154(elements)
               13045123 1073.949    0.000 1073.949    0.000 {built-in method torch._C._nn.one_hot}
              368340400  178.914    0.000 1040.673    0.000 {built-in method builtins.all}
                3690932   20.516    0.000  978.016    0.000 level.py:8(__init__)
             2095054562  516.042    0.000  902.806    0.000 layers.py:799(<genexpr>)
                3683403   68.174    0.000  862.917    0.000 replaybuffer.py:18(stacker)
                3683403   70.217    0.000  832.875    0.000 replaybuffer.py:63(stacker)
             9112140228  811.469    0.000  811.469    0.000 layer.py:99(positions)
              103135284  795.436    0.000  795.436    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                3690932  117.149    0.000  774.942    0.000 levels.py:199(generate)
              368082052  556.810    0.000  725.821    0.000 layers.py:62(check)
              103135284  710.722    0.000  710.722    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
        9683726734/9683726731  593.653    0.000  660.168    0.000 {built-in method builtins.len}
              103135284  631.315    0.000  631.315    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              103135284  612.496    0.000  612.496    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              368082052  370.394    0.000  582.201    0.000 layers.py:273(check)
              368082052  363.530    0.000  576.373    0.000 layers.py:313(check)
                9361720  214.008    0.000  573.762    0.000 exploration.py:53(softmaxer)
              721947072  459.625    0.000  566.257    0.000 tensor.py:906(grad)
               14748670  210.581    0.000  547.994    0.000 random.py:315(sample)
                7381864   63.502    0.000  544.662    0.000 level.py:41(notUsed)
             7025811316  539.627    0.000  539.627    0.000 {built-in method builtins.hash}
                3683403  316.773    0.000  539.303    0.000 collector.py:46(collect)
                2003792  444.387    0.000  522.081    0.000 agent.py:187(convert_values)
              103135284  496.605    0.000  496.605    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              368082052  317.475    0.000  472.145    0.000 layers.py:48(check)
               11050209   14.353    0.000  449.739    0.000 loss.py:527(forward)
               11050209   41.710    0.000  435.386    0.000 functional.py:2898(mse_loss)
              368082052  261.865    0.000  388.309    0.000 layers.py:23(check)
              180841117  362.531    0.000  362.531    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               36909320   47.231    0.000  323.301    0.000 layer.py:77(restart)
              337395517  223.820    0.000  314.761    0.000 layer.py:134(remove)
             4063917019  314.662    0.000  314.662    0.000 {method 'random' of '_random.Random' objects}
              552376864  223.483    0.000  307.548    0.000 layer.py:138(add)
             2756022850  282.370    0.000  282.370    0.000 layer.py:211(isBlocking)
              448957166  189.127    0.000  277.077    0.000 random.py:250(_randbelow_with_getrandbits)
               73668070  271.291    0.000  271.291    0.000 layer.py:171(<listcomp>)
                7366808  270.352    0.000  270.352    0.000 {built-in method nonzero}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9606155: <Causal4_Conver4_2> in cluster <dcc> Done

Job <Causal4_Conver4_2> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Mon May  3 01:44:22 2021
Job was executed on host(s) <n-62-20-3>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Tue May  4 22:40:52 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Tue May  4 22:40:52 2021
Terminated at Wed May  5 22:36:09 2021
Results reported at Wed May  5 22:36:09 2021

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

    CPU time :                                   85904.48 sec.
    Max Memory :                                 10105 MB
    Average Memory :                             6609.49 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               6279.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86119 sec.
    Turnaround time :                            247907 sec.

The output (if any) is above this job summary.

