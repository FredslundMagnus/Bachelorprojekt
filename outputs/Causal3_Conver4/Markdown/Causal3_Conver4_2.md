
# Parameters

    Name :                      Causal3_Conver4-2
    Main :                      CFagent
    Level :                     Levels.Causal3
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


      71735761626 function calls (71367609203 primitive calls) in 86125.83 seconds

##    Ordered by: cumulative time
   List reduced from 509 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86125.830 86125.830 {built-in method builtins.exec}
                      1    4.556    4.556 86125.830 86125.830 <string>:1(<module>)
                      1  403.783  403.783 86121.274 86121.274 main.py:80(CFagent)
               11483796   42.575    0.000 26679.265    0.002 agent.py:29(learn)
               11483796  674.218    0.000 21697.183    0.002 learner.py:42(Qlearn)
                3827932   15.342    0.000 18834.066    0.005 game.py:42(step)
                3827932   20.815    0.000 18045.676    0.005 layers.py:827(step)
        411589733/43439001 1557.660    0.000 12762.538    0.000 module.py:866(_call_impl)
               31955205   81.990    0.000 11955.686    0.000 network.py:28(forward)
               31955205  378.153    0.000 11677.672    0.000 container.py:117(forward)
                3827932  320.944    0.000 11053.734    0.003 layers.py:17(step)
              382516938  603.588    0.000 10694.511    0.000 layer.py:106(move)
                3827932  388.888    0.000 10366.571    0.003 agent.py:54(_learn)
                3827932 1014.373    0.000 10142.060    0.003 agent.py:212(counterfact)
                3827932  383.860    0.000 9508.813    0.002 agent.py:204(_learn)
               11483796   94.173    0.000 8501.928    0.001 optimizer.py:84(wrapper)
               11483796   46.336    0.000 8083.416    0.001 grad_mode.py:24(decorate_context)
               11483796  322.490    0.000 7934.601    0.001 adam.py:55(step)
               11483796 1644.368    0.000 7240.946    0.001 _functional.py:53(adam)
                3827933  534.416    0.000 6940.141    0.002 layers.py:793(update)
                3827932  112.785    0.000 6736.986    0.002 agent.py:117(_learn)
                3827932 5440.092    0.001 6573.917    0.002 replaybuffer.py:22(sample_data)
              382516938 1369.361    0.000 6342.978    0.000 layers.py:844(check)
                3827932 5248.607    0.001 6342.528    0.002 replaybuffer.py:67(sample_data)
               10233162  254.209    0.000 6256.719    0.001 agent.py:49(__call__)
               11483796   43.918    0.000 5579.439    0.000 tensor.py:195(backward)
               11483796   40.781    0.000 5534.114    0.000 __init__.py:68(backward)
                3827932 3007.613    0.001 5291.031    0.001 replaybuffer.py:28(teleporter_save_data)
               11483796 5281.633    0.000 5281.633    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
                3827932 2604.805    0.001 4930.855    0.001 agent.py:88(interveen)
               55019339 4679.615    0.000 4679.615    0.000 {built-in method tensor}
               46256573   26.535    0.000 4478.534    0.000 game.py:38(board)
               63910410  133.521    0.000 4328.483    0.000 conv.py:398(forward)
               63910410   90.494    0.000 4132.696    0.000 conv.py:390(_conv_forward)
               63910410 4042.201    0.000 4042.201    0.000 {built-in method conv2d}
               61246920 2050.545    0.000 3655.725    0.000 layer.py:175(NoRock_update)
                2582383   51.956    0.000 3398.754    0.001 agent.py:176(choose_action)
               88209751  175.338    0.000 3315.439    0.000 linear.py:93(forward)
              382516938  565.592    0.000 3169.426    0.000 layers.py:838(isFree)
               88209751   66.617    0.000 3057.146    0.000 functional.py:1737(linear)
               88209751 2974.479    0.000 2974.479    0.000 {built-in method torch._C._nn.linear}
                3827932 1782.418    0.000 2686.033    0.001 agent.py:67(modify)
             2818398530 2143.577    0.000 2603.834    0.000 layer.py:103(isFree)
              238866829 2199.914    0.000 2199.914    0.000 {built-in method clone}
               52340414 1858.011    0.000 1858.011    0.000 {built-in method cat}
                5394872   59.915    0.000 1757.139    0.000 layers.py:849(restart)
              120164956   92.871    0.000 1750.100    0.000 activation.py:713(forward)
               14061094   84.235    0.000 1736.093    0.000 agent.py:59(modify_board)
              120164956   89.716    0.000 1657.230    0.000 functional.py:1364(leaky_relu)
                3827932   61.941    0.000 1626.034    0.000 agent.py:172(__call__)
                3827932 1204.338    0.000 1561.636    0.000 replaybuffer.py:73(CF_save_data)
              120164956 1549.107    0.000 1549.107    0.000 {built-in method torch._C._nn.leaky_relu}
                3827932   57.522    0.000 1542.858    0.000 agent.py:112(__call__)
             5852004804 1017.907    0.000 1475.838    0.000 enum.py:646(__hash__)
              214364192 1430.644    0.000 1430.644    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              382516938  858.775    0.000 1374.871    0.000 layers.py:246(check)
              381226361  319.608    0.000 1342.121    0.000 {built-in method builtins.any}
               11483796  222.361    0.000 1263.001    0.000 optimizer.py:189(zero_grad)
                5394872   27.399    0.000 1259.756    0.000 level.py:8(__init__)
              214364192 1255.115    0.000 1255.115    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              382793300  178.683    0.000 1248.227    0.000 {built-in method builtins.all}
              382516938  710.018    0.000 1208.035    0.000 layers.py:286(check)
               14061094 1143.148    0.000 1143.148    0.000 {built-in method torch._C._nn.one_hot}
             2107560758  546.710    0.000 1114.591    0.000 layers.py:799(<genexpr>)
             3396585852  836.733    0.000 1022.513    0.000 layers.py:809(<genexpr>)
                5394872  106.379    0.000  981.678    0.000 levels.py:164(generate)
             1403596146  921.913    0.000  921.913    0.000 layer.py:154(elements)
                3827932   68.225    0.000  861.204    0.000 replaybuffer.py:18(stacker)
                3827932   70.447    0.000  831.531    0.000 replaybuffer.py:63(stacker)
              107182096  831.234    0.000  831.234    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               10789744  100.679    0.000  731.672    0.000 level.py:41(notUsed)
              107182096  725.210    0.000  725.210    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                2582383  605.980    0.000  703.707    0.000 agent.py:187(convert_values)
             7237902897  691.280    0.000  691.280    0.000 layer.py:99(positions)
              107182096  670.964    0.000  670.964    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              107182096  655.490    0.000  655.490    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
        8659838772/8659838769  559.857    0.000  628.832    0.000 {built-in method builtins.len}
               10233162  234.779    0.000  624.996    0.000 exploration.py:53(softmaxer)
               18445608  234.012    0.000  621.722    0.000 random.py:315(sample)
              382516938  378.281    0.000  608.838    0.000 layers.py:313(check)
              750274756  466.976    0.000  577.892    0.000 tensor.py:906(grad)
              382516938  358.168    0.000  574.943    0.000 layers.py:273(check)
                3827932  330.931    0.000  562.464    0.000 collector.py:46(collect)
              256755855  508.243    0.000  508.243    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              107182096  506.511    0.000  506.511    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              382516938  330.242    0.000  498.226    0.000 layers.py:48(check)
               11483796   18.577    0.000  466.813    0.000 loss.py:527(forward)
             5852048291  457.938    0.000  457.938    0.000 {built-in method builtins.hash}
               11483796   41.429    0.000  448.236    0.000 functional.py:2898(mse_loss)
               43158976   54.492    0.000  423.082    0.000 layer.py:77(restart)
              382516938  269.273    0.000  404.674    0.000 layers.py:23(check)
              642913296  260.414    0.000  357.089    0.000 layer.py:138(add)
              191060891  224.839    0.000  338.025    0.000 layers.py:113(isDone)
              519151451  229.160    0.000  335.825    0.000 random.py:250(_randbelow_with_getrandbits)
               10789744   11.600    0.000  317.363    0.000 level.py:38(elementsIn)
              369750673  219.055    0.000  315.144    0.000 layer.py:134(remove)
               63910410   42.732    0.000  282.993    0.000 flatten.py:39(forward)
                7655866  279.243    0.000  279.243    0.000 {built-in method nonzero}
               11483796  277.159    0.000  277.159    0.000 {built-in method torch._C._nn.mse_loss}
             3471571422  271.753    0.000  271.753    0.000 {method 'random' of '_random.Random' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9615515: <Causal3_Conver4_2> in cluster <dcc> Done

Job <Causal3_Conver4_2> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Tue May  4 23:51:56 2021
Job was executed on host(s) <n-62-20-3>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Wed May  5 22:36:11 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Wed May  5 22:36:11 2021
Terminated at Thu May  6 22:32:12 2021
Results reported at Thu May  6 22:32:12 2021

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

    CPU time :                                   85898.99 sec.
    Max Memory :                                 10732 MB
    Average Memory :                             7104.40 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               5652.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86162 sec.
    Turnaround time :                            168016 sec.

The output (if any) is above this job summary.

