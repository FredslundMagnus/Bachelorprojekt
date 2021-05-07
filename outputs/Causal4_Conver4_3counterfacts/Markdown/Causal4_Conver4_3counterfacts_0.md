
# Parameters

    Name :                      Causal4_Conver4_3counterfacts-0
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
    Counterfacts :              3
    Topn :                      5
    Random counterfacts :       False
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      60936546162 function calls (60623869607 primitive calls) in 86109.52 seconds

##    Ordered by: cumulative time
   List reduced from 515 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86109.524 86109.524 {built-in method builtins.exec}
                      1    4.717    4.717 86109.524 86109.524 <string>:1(<module>)
                      1  339.668  339.668 86104.807 86104.807 main.py:80(CFagent)
                2540680 2312.775    0.001 24520.112    0.010 agent.py:212(counterfact)
                7622040   36.344    0.000 19808.945    0.003 agent.py:29(learn)
                2540680   14.780    0.000 16872.019    0.007 game.py:42(step)
                2540680   18.351    0.000 16243.519    0.006 layers.py:827(step)
                7622034  509.429    0.000 16030.460    0.002 learner.py:42(Qlearn)
        347200030/34525166 1456.689    0.000 11667.279    0.000 module.py:866(_call_impl)
              100833886 11244.431    0.000 11244.431    0.000 {built-in method tensor}
               94911506   51.887    0.000 11117.000    0.000 game.py:38(board)
               26903132   79.765    0.000 10981.088    0.000 network.py:28(forward)
               26903132  368.660    0.000 10712.039    0.000 container.py:117(forward)
                2540680  254.174    0.000 10692.971    0.004 layers.py:17(step)
              252717692  770.556    0.000 10415.973    0.000 layer.py:106(move)
                2540680  313.203    0.000 7715.675    0.003 agent.py:54(_learn)
                2540680  305.991    0.000 6994.241    0.003 agent.py:204(_learn)
                2540680 5816.803    0.002 6694.457    0.003 replaybuffer.py:22(sample_data)
              101627190 3699.595    0.000 6526.191    0.000 layer.py:159(update)
                2540680 5612.794    0.002 6447.728    0.003 replaybuffer.py:67(sample_data)
                9638888  286.447    0.000 6442.122    0.001 agent.py:49(__call__)
                4560856   92.897    0.000 6342.834    0.001 agent.py:176(choose_action)
              252717692 1237.557    0.000 6337.587    0.000 layers.py:844(check)
                7622034   76.964    0.000 6196.716    0.001 optimizer.py:84(wrapper)
                7622034   42.814    0.000 5869.592    0.001 grad_mode.py:24(decorate_context)
                7622034  258.250    0.000 5740.419    0.001 adam.py:55(step)
                2540681  402.325    0.000 5506.078    0.002 layers.py:793(update)
                7622034 1206.507    0.000 5208.639    0.001 _functional.py:53(adam)
                2540680   85.617    0.000 5043.634    0.002 agent.py:117(_learn)
                7622034   35.236    0.000 4224.607    0.001 tensor.py:195(backward)
                7622034   42.531    0.000 4188.248    0.001 __init__.py:68(backward)
                7622034 3977.643    0.001 3977.643    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
               53806264  120.279    0.000 3962.725    0.000 conv.py:398(forward)
               53806264   81.475    0.000 3782.419    0.000 conv.py:390(_conv_forward)
               53806264 3700.944    0.000 3700.944    0.000 {built-in method conv2d}
                2540680 1576.228    0.001 3273.181    0.001 agent.py:88(interveen)
                2540680 1801.440    0.001 3084.121    0.001 replaybuffer.py:28(teleporter_save_data)
               75628036  155.253    0.000 3014.705    0.000 linear.py:93(forward)
              252717692  526.897    0.000 2793.613    0.000 layers.py:838(isFree)
               75628036   62.620    0.000 2776.315    0.000 functional.py:1737(linear)
               75628036 2698.836    0.000 2698.836    0.000 {built-in method torch._C._nn.linear}
             2283072483 1900.378    0.000 2266.715    0.000 layer.py:103(isFree)
                2540680 1326.972    0.001 2009.154    0.001 agent.py:67(modify)
               12179568   78.800    0.000 1644.718    0.000 agent.py:59(modify_board)
              102531168   84.592    0.000 1580.231    0.000 activation.py:713(forward)
             1016698354 1567.418    0.000 1567.418    0.000 layer.py:154(elements)
               37586338 1497.115    0.000 1497.115    0.000 {built-in method cat}
              102531168   81.540    0.000 1495.639    0.000 functional.py:1364(leaky_relu)
              102531168 1395.887    0.000 1395.887    0.000 {built-in method torch._C._nn.leaky_relu}
             5107944561  917.223    0.000 1330.022    0.000 enum.py:646(__hash__)
                4560856 1102.078    0.000 1280.198    0.000 agent.py:187(convert_values)
              123257825 1260.473    0.000 1260.473    0.000 {built-in method clone}
                3016371   44.918    0.000 1218.609    0.000 layers.py:849(restart)
                2540674   53.506    0.000 1204.627    0.000 agent.py:172(__call__)
                2540680   52.795    0.000 1145.917    0.000 agent.py:112(__call__)
              258673768  267.485    0.000 1142.749    0.000 {built-in method builtins.any}
               12179568 1083.107    0.000 1083.107    0.000 {built-in method torch._C._nn.one_hot}
                2540680  828.094    0.000 1053.030    0.000 replaybuffer.py:73(CF_save_data)
              142277960 1036.854    0.000 1036.854    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              252717692  780.216    0.000 1020.327    0.000 layers.py:77(check)
              252717692  591.897    0.000  911.182    0.000 layers.py:286(check)
                7622034  160.275    0.000  891.303    0.000 optimizer.py:189(zero_grad)
              142277960  886.432    0.000  886.432    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                3016371   18.382    0.000  875.972    0.000 level.py:8(__init__)
             2761569019  722.938    0.000  875.264    0.000 layers.py:809(<genexpr>)
        12163868927/12163868924  740.906    0.000  809.931    0.000 {built-in method builtins.len}
              252717692  481.558    0.000  790.469    0.000 layers.py:246(check)
              254068100   72.924    0.000  752.887    0.000 {built-in method builtins.all}
              780340435  206.245    0.000  711.987    0.000 layers.py:799(<genexpr>)
                3016371  105.844    0.000  691.877    0.000 levels.py:199(generate)
                2540680   58.344    0.000  665.487    0.000 replaybuffer.py:18(stacker)
                9638888  240.842    0.000  654.655    0.000 exploration.py:53(softmaxer)
                2540674   59.545    0.000  632.973    0.000 replaybuffer.py:63(stacker)
             6537760924  626.681    0.000  626.681    0.000 layer.py:99(positions)
              252717692  473.286    0.000  602.185    0.000 layers.py:62(check)
               71138980  591.990    0.000  591.990    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               71138980  522.757    0.000  522.757    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                6032742   55.619    0.000  482.942    0.000 level.py:41(notUsed)
              254068100  331.905    0.000  480.463    0.000 layers.py:113(isDone)
               71138980  478.568    0.000  478.568    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               71138980  465.067    0.000  465.067    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               11114102  179.603    0.000  455.666    0.000 random.py:315(sample)
              252717692  298.450    0.000  455.082    0.000 layers.py:313(check)
              101627190  423.651    0.000  423.651    0.000 layer.py:171(<listcomp>)
              497972944  337.188    0.000  417.644    0.000 tensor.py:906(grad)
              252717692  265.721    0.000  413.103    0.000 layers.py:273(check)
             5107973712  412.805    0.000  412.805    0.000 {built-in method builtins.hash}
                2540680  237.966    0.000  404.335    0.000 collector.py:46(collect)
                7622034   16.091    0.000  380.934    0.000 loss.py:527(forward)
              252717692  248.943    0.000  367.667    0.000 layers.py:48(check)
                7622034   39.970    0.000  364.843    0.000 functional.py:2898(mse_loss)
               71138980  352.632    0.000  352.632    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              101627190  321.144    0.000  321.144    0.000 layer.py:172(<listcomp>)
              232747252  245.555    0.000  320.101    0.000 layer.py:134(remove)
              137978067  306.336    0.000  306.336    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              252717692  197.510    0.000  287.846    0.000 layers.py:23(check)
               30163710   43.306    0.000  287.323    0.000 layer.py:77(restart)
               53806264   37.972    0.000  255.404    0.000 flatten.py:39(forward)
              407653989  170.295    0.000  244.321    0.000 layer.py:138(add)
               18206303  239.089    0.000  239.089    0.000 {method 'item' of 'torch._C._TensorBase' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9618555: <Causal4_Conver4_3counterfacts_0> in cluster <dcc> Done

Job <Causal4_Conver4_3counterfacts_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Thu May  6 00:28:48 2021
Job was executed on host(s) <n-62-20-11>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Thu May  6 03:21:57 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Thu May  6 03:21:57 2021
Terminated at Fri May  7 03:17:11 2021
Results reported at Fri May  7 03:17:11 2021

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

    CPU time :                                   85796.52 sec.
    Max Memory :                                 7826 MB
    Average Memory :                             5476.34 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               8558.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86138 sec.
    Turnaround time :                            96503 sec.

The output (if any) is above this job summary.

