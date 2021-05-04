
# Parameters

    Name :                      Causal4_Conver3-0
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
    Cf convert :                3
    Counterfacts :              1
    Topn :                      3
    Random counterfacts :       False
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      69976204079 function calls (69671111456 primitive calls) in 86109.20 seconds

##    Ordered by: cumulative time
   List reduced from 514 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86109.197 86109.197 {built-in method builtins.exec}
                      1    4.641    4.641 86109.197 86109.197 <string>:1(<module>)
                      1  359.848  359.848 86104.556 86104.556 main.py:80(CFagent)
                9891960   38.949    0.000 29813.881    0.003 agent.py:29(learn)
                9891960  745.706    0.000 24818.638    0.003 learner.py:42(Qlearn)
                3297320   15.177    0.000 19568.244    0.006 game.py:42(step)
                3297320   19.545    0.000 18742.634    0.006 layers.py:827(step)
        341506243/36415311 1416.292    0.000 12773.011    0.000 module.py:866(_call_impl)
                3297320  275.522    0.000 12421.624    0.004 layers.py:17(step)
              329493775  896.812    0.000 12115.306    0.000 layer.py:106(move)
               26523351   73.428    0.000 11976.367    0.000 network.py:28(forward)
               26523351  379.944    0.000 11733.626    0.000 container.py:117(forward)
                3297320  348.186    0.000 11499.263    0.003 agent.py:54(_learn)
                3297320  343.942    0.000 10658.571    0.003 agent.py:204(_learn)
                9891960   87.187    0.000 10487.918    0.001 optimizer.py:84(wrapper)
                3297320  964.457    0.000 10269.954    0.003 agent.py:212(counterfact)
                9891960   42.211    0.000 10083.584    0.001 grad_mode.py:24(decorate_context)
                9891960  303.087    0.000 9950.073    0.001 adam.py:55(step)
                9891960 2057.255    0.000 9313.532    0.001 _functional.py:53(adam)
                3297320  101.311    0.000 7596.134    0.002 agent.py:117(_learn)
              329493775 1478.389    0.000 7525.498    0.000 layers.py:844(check)
                3297321  465.495    0.000 6274.839    0.002 layers.py:793(update)
                9891960   42.158    0.000 6152.113    0.001 tensor.py:195(backward)
                9891960   37.246    0.000 6108.534    0.001 __init__.py:68(backward)
                8308444  220.532    0.000 6069.099    0.001 agent.py:49(__call__)
                9891960 5850.261    0.001 5850.261    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                3297320 4553.839    0.001 5651.494    0.002 replaybuffer.py:22(sample_data)
               52216240 5585.811    0.000 5585.811    0.000 {built-in method tensor}
                3297320 4337.660    0.001 5393.312    0.002 replaybuffer.py:67(sample_data)
               44624295   28.668    0.000 5362.479    0.000 game.py:38(board)
                3297320 1872.204    0.001 4264.862    0.001 agent.py:88(interveen)
               53046702  117.288    0.000 4233.065    0.000 conv.py:398(forward)
               53046702   73.799    0.000 4061.718    0.000 conv.py:390(_conv_forward)
               65946410 2346.112    0.000 4020.083    0.000 layer.py:159(update)
               53046702 3987.919    0.000 3987.919    0.000 {built-in method conv2d}
                3297320 1960.797    0.001 3668.712    0.001 replaybuffer.py:28(teleporter_save_data)
               72975413  145.361    0.000 3395.157    0.000 linear.py:93(forward)
               72975413   58.769    0.000 3175.333    0.000 functional.py:1737(linear)
               72975413 3101.511    0.000 3101.511    0.000 {built-in method torch._C._nn.linear}
              329493775  583.973    0.000 3097.674    0.000 layers.py:838(isFree)
                3297320 1894.645    0.001 2863.746    0.001 agent.py:67(modify)
                1728307   38.563    0.000 2616.102    0.002 agent.py:176(choose_action)
             3000964904 2049.922    0.000 2513.700    0.000 layer.py:103(isFree)
              184649920 1908.184    0.000 1908.184    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               99498764   81.416    0.000 1894.869    0.000 activation.py:713(forward)
               44578964 1875.549    0.000 1875.549    0.000 {built-in method cat}
               99498764   78.576    0.000 1813.453    0.000 functional.py:1364(leaky_relu)
               99498764 1717.135    0.000 1717.135    0.000 {built-in method torch._C._nn.leaky_relu}
               11605764   79.308    0.000 1691.768    0.000 agent.py:59(modify_board)
                3297320   60.468    0.000 1686.006    0.001 agent.py:172(__call__)
              184649920 1677.145    0.000 1677.145    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              126507595 1672.102    0.000 1672.102    0.000 {built-in method clone}
             6276321929 1103.359    0.000 1577.278    0.000 enum.py:646(__hash__)
                3297320   57.851    0.000 1568.954    0.000 agent.py:112(__call__)
                9891960  237.082    0.000 1469.860    0.000 optimizer.py:189(zero_grad)
              329701273  328.133    0.000 1415.707    0.000 {built-in method builtins.any}
                3297320 1087.005    0.000 1406.819    0.000 replaybuffer.py:73(CF_save_data)
                3328148   41.748    0.000 1221.447    0.000 layers.py:849(restart)
              329493775  901.885    0.000 1186.206    0.000 layers.py:77(check)
             3590443472  904.684    0.000 1087.573    0.000 layers.py:809(<genexpr>)
              329493775  695.263    0.000 1087.498    0.000 layers.py:246(check)
               11605764 1078.643    0.000 1078.643    0.000 {built-in method torch._C._nn.one_hot}
               92324960 1033.557    0.000 1033.557    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              329493775  573.913    0.000  946.224    0.000 layers.py:286(check)
             1098848278  933.836    0.000  933.836    0.000 layer.py:154(elements)
               92324960  904.878    0.000  904.878    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              329732100  160.159    0.000  898.647    0.000 {built-in method builtins.all}
                3328148   19.246    0.000  879.196    0.000 level.py:8(__init__)
                3297320   63.768    0.000  863.832    0.000 replaybuffer.py:18(stacker)
               92324960  862.752    0.000  862.752    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               92324960  843.000    0.000  843.000    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                3297320   66.552    0.000  830.703    0.000 replaybuffer.py:63(stacker)
             1873937960  458.539    0.000  775.886    0.000 layers.py:799(<genexpr>)
                3328148  109.245    0.000  698.236    0.000 levels.py:199(generate)
             7990746048  691.387    0.000  691.387    0.000 layer.py:99(positions)
                3297320  417.502    0.000  689.023    0.000 collector.py:46(collect)
               92324960  671.162    0.000  671.162    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              329493775  507.014    0.000  653.222    0.000 layers.py:62(check)
                8308444  227.296    0.000  620.882    0.000 exploration.py:53(softmaxer)
        8694830674/8694830671  555.137    0.000  619.639    0.000 {built-in method builtins.len}
              329493775  378.042    0.000  582.024    0.000 layers.py:313(check)
              646274804  449.659    0.000  550.451    0.000 tensor.py:906(grad)
              329493775  338.932    0.000  530.601    0.000 layers.py:273(check)
               13250936  189.086    0.000  496.288    0.000 random.py:315(sample)
                9891960   14.383    0.000  491.428    0.000 loss.py:527(forward)
                6656296   55.041    0.000  485.928    0.000 level.py:41(notUsed)
                9891960   37.062    0.000  477.045    0.000 functional.py:2898(mse_loss)
             6276359480  473.925    0.000  473.925    0.000 {built-in method builtins.hash}
              141410679  458.304    0.000  458.304    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
                1728307  424.246    0.000  450.263    0.000 agent.py:187(convert_values)
              329493775  283.651    0.000  423.890    0.000 layers.py:48(check)
              329493775  227.666    0.000  340.083    0.000 layers.py:23(check)
                9891960  314.484    0.000  314.484    0.000 {built-in method torch._C._nn.mse_loss}
               53046702   36.435    0.000  309.349    0.000 flatten.py:39(forward)
               33281480   43.887    0.000  289.919    0.000 layer.py:77(restart)
               19783920  289.326    0.000  289.326    0.000 {built-in method sum}
                6594642  285.799    0.000  285.799    0.000 {built-in method nonzero}
                9893119  276.887    0.000  276.887    0.000 {built-in method max}
               53046702  272.914    0.000  272.914    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
             3637951514  270.755    0.000  270.755    0.000 {method 'random' of '_random.Random' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9606150: <Causal4_Conver3_0> in cluster <dcc> Done

Job <Causal4_Conver3_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Mon May  3 01:44:21 2021
Job was executed on host(s) <n-62-20-6>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Mon May  3 20:27:17 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Mon May  3 20:27:17 2021
Terminated at Tue May  4 20:22:31 2021
Results reported at Tue May  4 20:22:31 2021

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

    CPU time :                                   85900.66 sec.
    Max Memory :                                 9508 MB
    Average Memory :                             6346.51 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               6876.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86115 sec.
    Turnaround time :                            153490 sec.

The output (if any) is above this job summary.

